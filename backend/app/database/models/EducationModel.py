# models/education.py
from app.database.db import get_db
from bson.objectid import ObjectId

class Education:
    def __init__(self, candidate_id, institution, degree, field_of_study=None, start_date=None, end_date=None):
        self.candidate_id = candidate_id
        self.institution = institution
        self.degree = degree
        self.field_of_study = field_of_study
        self.start_date = start_date
        self.end_date = end_date

    def save(self):
        db = get_db()
        education_data = {
            "candidate_id": ObjectId(self.candidate_id),
            "institution": self.institution,
            "degree": self.degree,
            "field_of_study": self.field_of_study,
            "start_date": self.start_date,
            "end_date": self.end_date
        }
        return db.education.insert_one(education_data).inserted_id

    @staticmethod
    def find_by_candidate_id(candidate_id):
        db = get_db()
        return list(db.education.find({"candidate_id": ObjectId(candidate_id)}))

    @staticmethod
    def delete_by_id(education_id):
        db = get_db()
        return db.education.delete_one({"_id": ObjectId(education_id)})