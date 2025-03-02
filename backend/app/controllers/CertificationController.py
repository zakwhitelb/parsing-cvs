from app.database.models.CertificationModel import Certification

class CertificationController:
    @staticmethod
    def add_certification(candidate_id, certification_name, issuing_organization=None, issue_date=None, expiration_date=None):
        """
        Add a new certification for a candidate.
        """
        certification = Certification(candidate_id, certification_name, issuing_organization, issue_date, expiration_date)
        return certification.save()

    @staticmethod
    def get_certifications_by_candidate(candidate_id):
        """
        Retrieve all certifications for a specific candidate.
        """
        return Certification.find_by_candidate_id(candidate_id)

    @staticmethod
    def delete_certification(certification_id):
        """
        Delete a certification by its ID.
        """
        return Certification.delete_by_id(certification_id)

    @staticmethod
    def insert_data(certification_data):
        """
        Insert certification data into the database.
        Args:
            certification_data (dict): A dictionary containing certification data.
                                      Required fields: candidate_id, certification_name.
                                      Optional fields: issuing_organization, issue_date, expiration_date.
        Returns:
            The inserted certification's ID.
        """
        # Validate required fields
        if not certification_data.get("candidate_id") or not certification_data.get("certification_name"):
            raise ValueError("candidate_id and certification_name are required fields.")

        # Create a new Certification instance and save it
        certification = Certification(
            candidate_id=certification_data["candidate_id"],
            certification_name=certification_data["certification_name"],
            issuing_organization=certification_data.get("issuing_organization"),  # Optional
            issue_date=certification_data.get("issue_date"),  # Optional
            expiration_date=certification_data.get("expiration_date")  # Optional
        )
        return certification.save()