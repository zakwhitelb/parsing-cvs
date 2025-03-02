# app/api/cv_parser.py
from fastapi import APIRouter, HTTPException, Path
from app.controllers.CandidateController import CandidateController
from app.controllers.EducationController import EducationController
from app.controllers.WorkExperienceController import WorkExperienceController
from app.controllers.SkillController import SkillController
from app.controllers.CertificationController import CertificationController
from app.controllers.ProjectController import ProjectController
from app.utils.ObjectIdToStr import convert_objectid_to_str

router = APIRouter()

# Initialize controllers
candidate_controller = CandidateController()
education_controller = EducationController()
work_experience_controller = WorkExperienceController()
skill_controller = SkillController()
certification_controller = CertificationController()
project_controller = ProjectController()


@router.get("/get_data_by_candida_id/{candidate_id}", response_model=dict)
async def get_candidate_by_id(candidate_id: str = Path(..., description="The ID of the candidate")):
    """
    Get data for a single candidate by their ID.
    Args:
        candidate_id (str): The ID of the candidate.
    Returns:
        dict: A dictionary containing the candidate's data and their related information.
    Raises:
        HTTPException: If the candidate is not found.
    """
    candidate = candidate_controller.get_candidate(candidate_id)
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found.")

    # Convert ObjectId fields to strings in the candidate data
    candidate = convert_objectid_to_str(candidate)

    # Fetch related data and convert ObjectId fields to strings
    education = convert_objectid_to_str(education_controller.get_education_by_candidate(candidate_id))
    work_experience = convert_objectid_to_str(work_experience_controller.get_experience_by_candidate(candidate_id))
    skills = convert_objectid_to_str(skill_controller.get_skills_by_candidate(candidate_id))
    certifications = convert_objectid_to_str(certification_controller.get_certifications_by_candidate(candidate_id))
    projects = convert_objectid_to_str(project_controller.get_projects_by_candidate(candidate_id))

    candidate_data = {
        "candidate": candidate,
        "education": education,
        "work_experience": work_experience,
        "skills": skills,
        "certifications": certifications,
        "projects": projects,
    }

    return candidate_data