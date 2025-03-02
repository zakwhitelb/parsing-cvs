# models/project.py
from app.database.db import get_db
from bson.objectid import ObjectId

class Project:
    def __init__(self, candidate_id, project_name, description=None, start_date=None, end_date=None):
        self.candidate_id = candidate_id
        self.project_name = project_name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date

    def save(self):
        db = get_db()
        project_data = {
            "candidate_id": ObjectId(self.candidate_id),
            "project_name": self.project_name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date
        }
        return db.projects.insert_one(project_data).inserted_id

    @staticmethod
    def find_by_candidate_id(candidate_id):
        db = get_db()
        return list(db.projects.find({"candidate_id": ObjectId(candidate_id)}))

    @staticmethod
    def delete_by_id(project_id):
        db = get_db()
        return db.projects.delete_one({"_id": ObjectId(project_id)})