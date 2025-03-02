from app.database.models.EducationModel import Education

class EducationController:
    @staticmethod
    def add_education(candidate_id, institution, degree, field_of_study=None, start_date=None, end_date=None):
        """
        Add a new education record for a candidate.
        """
        education = Education(candidate_id, institution, degree, field_of_study, start_date, end_date)
        return education.save()

    @staticmethod
    def get_education_by_candidate(candidate_id):
        """
        Retrieve all education records for a specific candidate.
        """
        return Education.find_by_candidate_id(candidate_id)

    @staticmethod
    def delete_education(education_id):
        """
        Delete an education record by its ID.
        """
        return Education.delete_by_id(education_id)

    @staticmethod
    def insert_data(education_data):
        """
        Insert education data into the database.
        Args:
            education_data (dict): A dictionary containing education data.
                                   Required fields: candidate_id, institution, degree.
                                   Optional fields: field_of_study, start_date, end_date.
        Returns:
            The inserted education record's ID.
        """
        # Validate required fields
        if not education_data.get("candidate_id") or not education_data.get("institution") or not education_data.get("degree"):
            raise ValueError("candidate_id, institution, and degree are required fields.")

        # Create a new Education instance and save it
        education = Education(
            candidate_id=education_data["candidate_id"],
            institution=education_data["institution"],
            degree=education_data["degree"],
            field_of_study=education_data.get("field_of_study"),  # Optional
            start_date=education_data.get("start_date"),  # Optional
            end_date=education_data.get("end_date")  # Optional
        )
        return education.save()