# Routes/notes.py
from fastapi import APIRouter, Depends
from bson import ObjectId
from Database.Users.db import notes_collection
from Services.notes import noteCreate
from Models.notes import note_helper as note_model      
from Auth.Services.authService import get_current_user

router = APIRouter(prefix="/notes", tags=["Notes"])

@router.post('/note')
async def create_note_endpoint( 
    note: noteCreate,
    current_user: dict = Depends(get_current_user)
):
    note_data = dict(note)
    note_data['creatorId'] = str(current_user['_id']) 

    result = notes_collection.insert_one(note_data)
    new_note = notes_collection.find_one({"_id": result.inserted_id})
    
    if new_note:
        new_note["_id"] = str(new_note["_id"])
    
    note_obj = note_model(new_note)
    return {"message": "Note created successfully", "note": note_obj}

@router.get('/')
async def get_all_notes():
    notes = []
    for n in notes_collection.find():
        n["_id"] = str(n["_id"])
        notes.append(note_model(n))  
    return {"notes": notes}

@router.get('/my')
async def get_my_notes(current_user: dict = Depends(get_current_user)):   
    notes = list(notes_collection.find({"creatorId": str(current_user["_id"])}))
    for n in notes:
        n["_id"] = str(n["_id"])
    processed_notes = [note_model(n) for n in notes] 
    return {"notes": processed_notes}   

