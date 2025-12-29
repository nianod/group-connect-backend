from fastapi import APIRouter, Depends
from bsson import ObjectId
from Database.Users.db import notes_collection
from Models.notes import create_note as note_model
from Auth.Services.authService import get_current_user
