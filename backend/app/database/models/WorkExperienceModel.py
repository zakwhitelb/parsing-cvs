# models/work_experience.py
from app.database.db import get_db
from bson.objectid import ObjectId

class WorkExperience:
    def __init__(self, candidate_id, company, position, start_date=None, end_date=None, description=None):
        self.candidate_id = candidate_id
        self.company = company
        self.position = position
        self.start_date = start_date
        self.end_date = end_date
        self.description = description

    def save(self):
        db = get_db()
        experience_data = {
            "candidate_id": ObjectId(self.candidate_id),
            "company": self.company,
            "position": self.position,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description
        }
        return db.work_experience.insert_one(experience_data).inserted_id

    @staticmethod
    def find_by_candidate_id(candidate_id):
        db = get_db()
        return list(db.work_experience.find({"candidate_id": ObjectId(candidate_id)}))

    @staticmethod
    def delete_by_id(experience_id):
        db = get_db()
        return db.work_experience.delete_one({"_id": ObjectId(experience_id)})