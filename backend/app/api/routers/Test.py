import re
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

router = APIRouter()

class URLRequest(BaseModel):
    url: str

@router.post("/stock")
async def get_stock(req: URLRequest):
    """
    1) Rendre la page en headless avec Playwright async API :contentReference[oaicite:3]{index=3}
    2) Parser le HTML avec BeautifulSoup :contentReference[oaicite:4]{index=4}
    3) Extraire le nombre en stock via regex
    """
    # 1) Lancement du navigateur headless
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(req.url, timeout=30_000)
        html = await page.content()
        await browser.close()

    # 2) Parsing HTML
    soup = BeautifulSoup(html, "lxml")
    avail = soup.select_one("#availability .a-color-state, #availability .a-size-medium")
    if not avail:
        raise HTTPException(status_code=404, detail="Informations de stock introuvables")
    text = avail.get_text(strip=True)

    # 3) Extraction du nombre
    m = re.search(r"\d+", text)
    stock = int(m.group()) if m else text

    return {"url": req.url, "stock": stock}
