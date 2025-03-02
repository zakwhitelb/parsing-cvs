from app.database.models.SkillModel import Skill

class SkillController:
    @staticmethod
    def add_skill(candidate_id, skill_name, proficiency=None):
        """
        Add a new skill for a candidate.
        """
        skill = Skill(candidate_id, skill_name, proficiency)
        return skill.save()

    @staticmethod
    def get_skills_by_candidate(candidate_id):
        """
        Retrieve all skills for a specific candidate.
        """
        return Skill.find_by_candidate_id(candidate_id)

    @staticmethod
    def delete_skill(skill_id):
        """
        Delete a skill by its ID.
        """
        return Skill.delete_by_id(skill_id)

    @staticmethod
    def insert_data(skill_data):
        """
        Insert skill data into the database.
        Args:
            skill_data (dict): A dictionary containing skill data.
                              Required fields: candidate_id, skill_name.
                              Optional fields: proficiency.
        Returns:
            The inserted skill's ID.
        """
        # Validate required fields
        if not skill_data.get("candidate_id") or not skill_data.get("skill_name"):
            raise ValueError("candidate_id and skill_name are required fields.")

        # Create a new Skill instance and save it
        skill = Skill(
            candidate_id=skill_data["candidate_id"],
            skill_name=skill_data["skill_name"],
            proficiency=skill_data.get("proficiency")  # Optional
        )
        return skill.save()