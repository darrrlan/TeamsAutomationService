from pymongo import MongoClient
from datetime import datetime
from config import client

db = client['teams_microservice']
logs_collection = db['logs']

def log_event(action: str, status: str, details: dict = None):
    log_doc = {
        "action": action,
        "status": status,
        "details": details or {},
        "timestamp": datetime.utcnow()
    }
    result = logs_collection.insert_one(log_doc)
    return result.inserted_id
