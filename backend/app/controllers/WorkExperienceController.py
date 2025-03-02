from app.database.models.WorkExperienceModel import WorkExperience

class WorkExperienceController:
    @staticmethod
    def add_experience(candidate_id, company, position, start_date=None, end_date=None, description=None):
        """
        Add a new work experience record for a candidate.
        """
        experience = WorkExperience(candidate_id, company, position, start_date, end_date, description)
        return experience.save()

    @staticmethod
    def get_experience_by_candidate(candidate_id):
        """
        Retrieve all work experience records for a specific candidate.
        """
        return WorkExperience.find_by_candidate_id(candidate_id)

    @staticmethod
    def delete_experience(experience_id):
        """
        Delete a work experience record by its ID.
        """
        return WorkExperience.delete_by_id(experience_id)

    @staticmethod
    def insert_data(experience_data):
        """
        Insert work experience data into the database.
        Args:
            experience_data (dict): A dictionary containing work experience data.
                                   Required fields: candidate_id, company, position.
                                   Optional fields: start_date, end_date, description.
        Returns:
            The inserted work experience record's ID.
        """
        # Validate required fields
        if not experience_data.get("candidate_id") or not experience_data.get("company") or not experience_data.get("position"):
            raise ValueError("candidate_id, company, and position are required fields.")

        # Create a new WorkExperience instance and save it
        experience = WorkExperience(
            candidate_id=experience_data["candidate_id"],
            company=experience_data["company"],
            position=experience_data["position"],
            start_date=experience_data.get("start_date"),  # Optional
            end_date=experience_data.get("end_date"),  # Optional
            description=experience_data.get("description")  # Optional
        )
        return experience.save()