from app.database.models.CandidateModel import Candidate

class CandidateController:
    @staticmethod
    def create_candidate(name, email, phone=None):
        """
        Create a new candidate and save it to the database.
        """
        candidate = Candidate(name, email, phone)
        return candidate.save()

    @staticmethod
    def get_candidate(candidate_id):
        """
        Retrieve a candidate by their ID.
        """
        return Candidate.find_by_id(candidate_id)

    @staticmethod
    def get_all_candidates():
        """
        Retrieve all candidates from the database.
        """
        return Candidate.find_all()

    @staticmethod
    def delete_candidate(candidate_id):
        """
        Delete a candidate by their ID.
        """
        return Candidate.delete_by_id(candidate_id)

    @staticmethod
    def insert_data(candidate_data):
        """
        Insert candidate data into the database.
        Args:
            candidate_data (dict): A dictionary containing candidate data (name, email, phone, etc.).
        Returns:
            The inserted candidate's ID.
        """
        # Validate required fields
        if not candidate_data.get("name") or not candidate_data.get("email"):
            raise ValueError("Name and email are required fields.")

        # Create a new Candidate instance and save it
        candidate = Candidate(
            name=candidate_data["name"],
            email=candidate_data["email"],
            phone=candidate_data.get("phone")  # Optional field
        )
        return candidate.save()