# models/candidate.py
from app.database.db import get_db
from bson.objectid import ObjectId
from datetime import datetime

class Candidate:
    def __init__(self, name, email, phone=None, created_at=datetime.now()):
        self.name = name
        self.email = email
        self.phone = phone
        self.created_at = created_at

    def save(self):
        db = get_db()
        candidate_data = {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "created_at": self.created_at
        }
        return db.candidates.insert_one(candidate_data).inserted_id

    @staticmethod
    def find_by_id(candidate_id):
        db = get_db()
        return db.candidates.find_one({"_id": ObjectId(candidate_id)})

    @staticmethod
    def find_all():
        db = get_db()
        return list(db.candidates.find())

    @staticmethod
    def delete_by_id(candidate_id):
        db = get_db()
        return db.candidates.delete_one({"_id": ObjectId(candidate_id)})