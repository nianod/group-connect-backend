from fastapi import APIRouter, Depends
from bson import ObjectId
from Database.Users.db import notes_collection
from Services.notes import noteCreate
from Models.notes import note_helper
from Auth.Services.authService import get_current_user   

router = APIRouter(prefix="/notes", tags=["Notes"])

@router.post("/create")
def create_note(
    note: noteCreate,
    current_user: dict = Depends(get_current_user)
):
    note_data = note.dict()
    note_data['creatorId'] = str(current_user['_id'])

    result = notes_collection.insert_one(note_data)
    new_note = notes_collection.find_one({"_id": result.inserted_id})
    return {"message": "Note created successfully", "note": note_helper(new_note)}

@router.get("/")
def get_all_notes():
    notes = [note_helper(g) for g in notes_collection.find({} )]
    return {"notes": notes}

@router.get("/my")
def get_my_notes(current_user=Depends(get_current_user)):
    notes = list(notes_collection.find({"creatorId": str(current_user["_id"])}))
    for g in notes:
        g["_id"] = str(g["_id"])
    return notes

