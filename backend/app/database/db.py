# database/db.py
from pymongo import MongoClient

# Database connection settings
MONGO_URI = 'mongodb://localhost:27017'
DATABASE_NAME = 'candidate_database'

# Create a global connection and database object
client = MongoClient(MONGO_URI)

db = client[DATABASE_NAME]

def get_db():
    return db