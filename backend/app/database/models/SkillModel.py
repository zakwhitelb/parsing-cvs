# models/skill.py
from app.database.db import get_db
from bson.objectid import ObjectId

class Skill:
    def __init__(self, candidate_id, skill_name, proficiency=None):
        self.candidate_id = candidate_id
        self.skill_name = skill_name
        self.proficiency = proficiency

    def save(self):
        db = get_db()
        skill_data = {
            "candidate_id": ObjectId(self.candidate_id),
            "skill_name": self.skill_name,
            "proficiency": self.proficiency
        }
        return db.skills.insert_one(skill_data).inserted_id

    @staticmethod
    def find_by_candidate_id(candidate_id):
        db = get_db()
        return list(db.skills.find({"candidate_id": ObjectId(candidate_id)}))

    @staticmethod
    def delete_by_id(skill_id):
        db = get_db()
        return db.skills.delete_one({"_id": ObjectId(skill_id)})