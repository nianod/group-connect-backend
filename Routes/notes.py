from fastapi import APIRouter
from bson import ObjectId
from Database.Users.db import notes_collection
from Services.notes import noteCreate
from Models.notes import create_note

