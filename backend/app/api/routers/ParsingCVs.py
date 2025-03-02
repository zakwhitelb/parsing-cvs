from fastapi import APIRouter, HTTPException, File, UploadFile
from app.services.AllAccessor import AllAccessor
from typing import List

router = APIRouter()

@router.post("/parsing_cvs")
async def parse_cvs(files: List[UploadFile] = File(...)):
    if not files:
        raise HTTPException(status_code=400, detail="No files were uploaded.")

    all_accessor = AllAccessor()
    result = await all_accessor.get_cv_data_json_format(files)
    return {"data": result}
