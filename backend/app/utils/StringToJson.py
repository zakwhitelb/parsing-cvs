import json
from typing import Dict, List, Any

class StringToJson:
    def __init__(self, input_string: str):
        """
        Initialize the StringToJson class with the input string.
        Args:
            input_string (str): The input string containing the CV data.
        """
        self.input_string = input_string

    def to_json(self) -> Dict[str, Any]:
        """
        Convert the input string to a JSON object.
        Returns:
            Dict[str, Any]: A dictionary representing the JSON structure.
        Raises:
            ValueError: If the input string cannot be parsed as JSON.
        """
        try:
            # Parse the input string into a Python dictionary
            json_data = json.loads(self.input_string)
            return json_data
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse input string as JSON: {e}")

    def get_cv_data(self) -> List[Dict[str, Any]]:
        """
        Extract CV data from the JSON object.
        Returns:
            List[Dict[str, Any]]: A list of dictionaries, each representing a CV.
        """
        json_data = self.to_json()
        if "data" in json_data:
            return list(json_data["data"].values())  # Extract CVs from the "data" key
        return []
    
if(__name__ == "__main__"):
    # Example input string (valid JSON)
    input_string = '''
    {
    "data": {
        "cv 1": {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "123-456-7890",
        "education": [
            {
            "institution": "Harvard University",
            "degree": "Bachelor of Science",
            "field_of_study": "Computer Science",
            "start_date": "2015-09-01",
            "end_date": "2019-06-01"
            }
        ],
        "work_experience": [
            {
            "company": "Tech Corp",
            "position": "Software Engineer",
            "start_date": "2020-01-01",
            "end_date": "2022-12-31",
            "description": "Developed and maintained web applications using Python and Django."
            }
        ],
        "skills": [
            {
            "skill_name": "Python",
            "proficiency": "Expert"
            }
        ],
        "languages": [
            {
            "language": "English",
            "proficiency": "Fluent"
            }
        ],
        "certifications": [
            {
            "certification_name": "AWS Certified Solutions Architect",
            "issuing_organization": "Amazon Web Services",
            "issue_date": "2023-01-01",
            "expiration_date": "2026-01-01"
            }
        ],
        "projects": [
            {
            "project_name": "E-commerce Website",
            "description": "Developed a full-stack e-commerce website using React and Node.js.",
            "start_date": "2021-01-01",
            "end_date": "2021-06-01"
            }
        ],
        "volunteer_experience": [
            {
            "organization": "Local Charity",
            "role": "Volunteer",
            "start_date": "2018-01-01",
            "end_date": "2018-12-31",
            "description": "Helped organize community events."
            }
        ],
        "other_information": [
            {
            "category": "Awards",
            "details": "Best Employee of the Year 2022"
            }
        ]
        },
        "cv 2": {
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "phone": "987-654-3210",
        "education": [],
        "work_experience": [],
        "skills": [],
        "languages": [],
        "certifications": [],
        "projects": [],
        "volunteer_experience": [],
        "other_information": []
        }
    }
    }
    '''

    # Create an instance of StringToJson
    string_to_json = StringToJson(input_string)

    # Convert the string to JSON
    try:
        json_data = string_to_json.to_json()
        print("JSON Data:", json_data)

        # Extract CV data
        cv_data = string_to_json.get_cv_data()
        print("CV Data:", cv_data)
    except ValueError as e:
        print(e)