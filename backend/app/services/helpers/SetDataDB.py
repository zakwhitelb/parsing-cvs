from app.controllers.CandidateController import CandidateController
from app.controllers.CertificationController import CertificationController
from app.controllers.EducationController import EducationController
from app.controllers.ProjectController import ProjectController
from app.controllers.SkillController import SkillController
from app.controllers.WorkExperienceController import WorkExperienceController

from app.utils.StringToJson import StringToJson

class SetDataDB:
    def __init__(self):
        """
        Initialize the SetDataDB class with all the necessary controllers.
        """
        self.candidate_controller = CandidateController()
        self.certification_controller = CertificationController()
        self.education_controller = EducationController()
        self.project_controller = ProjectController()
        self.skill_controller = SkillController()
        self.work_experience_controller = WorkExperienceController()

    def insert_candidate_data(self, candidate_data: dict[str, any]) -> int:
        """
        Insert candidate data into the database.
        Args:
            candidate_data (Dict[str, Any]): A dictionary containing candidate data.
        Returns:
            int: The ID of the inserted candidate.
        """
        return self.candidate_controller.insert_data(candidate_data)

    def insert_education_data(self, candidate_id: int, education_data: list[dict[str, any]]):
        """
        Insert education data into the database.
        Args:
            candidate_id (int): The ID of the candidate.
            education_data (list[dict[str, any]]): A list of dictionaries containing education data.
        """
        for education in education_data:
            education["candidate_id"] = candidate_id
            self.education_controller.insert_data(education)

    def insert_work_experience_data(self, candidate_id: int, work_experience_data: list[dict[str, any]]):
        """
        Insert work experience data into the database.
        Args:
            candidate_id (int): The ID of the candidate.
            work_experience_data (list[dict[str, any]]): A list of dictionaries containing work experience data.
        """
        for experience in work_experience_data:
            experience["candidate_id"] = candidate_id
            self.work_experience_controller.insert_data(experience)

    def insert_skill_data(self, candidate_id: int, skill_data: list[dict[str, any]]):
        """
        Insert skill data into the database.
        Args:
            candidate_id (int): The ID of the candidate.
            skill_data (list[dict[str, any]]): A list of dictionaries containing skill data.
        """
        for skill in skill_data:
            skill["candidate_id"] = candidate_id
            self.skill_controller.insert_data(skill)

    def insert_certification_data(self, candidate_id: int, certification_data: list[dict[str, any]]):
        """
        Insert certification data into the database.
        Args:
            candidate_id (int): The ID of the candidate.
            certification_data (list[dict[str, any]]): A list of dictionaries containing certification data.
        """
        for certification in certification_data:
            certification["candidate_id"] = candidate_id
            self.certification_controller.insert_data(certification)

    def insert_project_data(self, candidate_id: int, project_data: list[dict[str, any]]):
        """
        Insert project data into the database.
        Args:
            candidate_id (int): The ID of the candidate.
            project_data (list[dict[str, any]]): A list of dictionaries containing project data.
        """
        for project in project_data:
            project["candidate_id"] = candidate_id
            self.project_controller.insert_data(project)

    def insert_all_data(self, cv_data: dict[str, any]):
        """
        Insert all CV data into the database.
        Args:
            cv_data (Dict[str, Any]): A dictionary containing all CV data.
        """
        # Insert candidate data
        candidate_id = self.insert_candidate_data({
            "name": cv_data["name"],
            "email": cv_data["email"],
            "phone": cv_data.get("phone")
        })

        # Insert education data
        if "education" in cv_data:
            self.insert_education_data(candidate_id, cv_data["education"])

        # Insert work experience data
        if "work_experience" in cv_data:
            self.insert_work_experience_data(candidate_id, cv_data["work_experience"])

        # Insert skill data
        if "skills" in cv_data:
            self.insert_skill_data(candidate_id, cv_data["skills"])

        # Insert certification data
        if "certifications" in cv_data:
            self.insert_certification_data(candidate_id, cv_data["certifications"])

        # Insert project data
        if "projects" in cv_data:
            self.insert_project_data(candidate_id, cv_data["projects"])

    def process_json_data(self, json_data: dict[str, any]):
        """
        Process the JSON data and insert it into the database.
        Args:
            json_data (Dict[str, Any]): The JSON data containing multiple CVs.
        """
        if "data" in json_data:
            for cv_key, cv_data in json_data["data"].items():
                self.insert_all_data(cv_data)

# Example usage
input_string = '''
{
    "data": {
        "cv 1": {
            "name": "Full name of the candidate",
            "email": "Email address of the candidate",
            "phone": "Phone number of the candidate",
            "education": [
                {
                    "institution": "Name of the educational institution",
                    "degree": "Degree obtained",
                    "field_of_study": "Field of study",
                    "start_date": "Start date of the education (YYYY-MM-DD)",
                    "end_date": "End date of the education (YYYY-MM-DD)"
                }
            ],
            "work_experience": [
                {
                    "company": "Name of the company",
                    "position": "Job title or position held",
                    "start_date": "Start date of the job (YYYY-MM-DD)",
                    "end_date": "End date of the job (YYYY-MM-DD)",
                    "description": "Description of the role and responsibilities"
                }
            ],
            "skills": [
                {
                    "skill_name": "Name of the skill",
                    "proficiency": "Proficiency level (e.g., Beginner, Intermediate, Expert)"
                }
            ],
            "certifications": [
                {
                    "certification_name": "Name of the certification",
                    "issuing_organization": "Organization that issued the certification",
                    "issue_date": "Date the certification was issued (YYYY-MM-DD)",
                    "expiration_date": "Expiration date of the certification (YYYY-MM-DD)"
                }
            ],
            "projects": [
                {
                    "project_name": "Name of the project",
                    "description": "Description of the project",
                    "start_date": "Start date of the project (YYYY-MM-DD)",
                    "end_date": "End date of the project (YYYY-MM-DD)"
                }
            ]
        }
    }
}
'''

# Convert the input string to JSON
string_to_json = StringToJson(input_string)
json_data = string_to_json.to_json()

# Insert the data into the database
set_data_db = SetDataDB()
set_data_db.process_json_data(json_data)