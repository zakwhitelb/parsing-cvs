# models/certification.py
from app.database.db import get_db
from bson.objectid import ObjectId

class Certification:
    def __init__(self, candidate_id, certification_name, issuing_organization=None, issue_date=None, expiration_date=None):
        self.candidate_id = candidate_id
        self.certification_name = certification_name
        self.issuing_organization = issuing_organization
        self.issue_date = issue_date
        self.expiration_date = expiration_date

    def save(self):
        db = get_db()
        certification_data = {
            "candidate_id": ObjectId(self.candidate_id),
            "certification_name": self.certification_name,
            "issuing_organization": self.issuing_organization,
            "issue_date": self.issue_date,
            "expiration_date": self.expiration_date
        }
        return db.certifications.insert_one(certification_data).inserted_id

    @staticmethod
    def find_by_candidate_id(candidate_id):
        db = get_db()
        return list(db.certifications.find({"candidate_id": ObjectId(candidate_id)}))

    @staticmethod
    def delete_by_id(certification_id):
        db = get_db()
        return db.certifications.delete_one({"_id": ObjectId(certification_id)})