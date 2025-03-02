# app/api/cv_parser.py
from fastapi import APIRouter
from typing import List
from app.controllers.CandidateController import CandidateController
from app.utils.ObjectIdToStr import convert_objectid_to_str

router = APIRouter()

# Initialize controllers
candidate_controller = CandidateController()

@router.get("/get_all_candida_data", response_model=List[dict])
async def get_all_candidates():
    """
    Get data for all candidates from the Candidate table.
    Returns:
        List[dict]: A list of dictionaries containing candidate data.
    """
    candidates = candidate_controller.get_all_candidates()
    # Convert ObjectId fields to strings
    candidates = convert_objectid_to_str(candidates)
    return candidates