# Database/Users/db.py
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

# Fail fast: timeout in 5 seconds if Mongo is unreachable
client = MongoClient(
    MONGO_URL,
    serverSelectionTimeoutMS=5000,   # <-- KEY FIX
)

db = client["group_connect"]

users_collection = db["users"]
groups_collection = db["group-create"]
