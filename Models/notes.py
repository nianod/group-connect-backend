# Models/notes.py
from bson import ObjectId

def note_helper(note_data) -> dict:
    return {
        "id": str(note_data["_id"]),
        "title": note_data["title"],
        "content": note_data["content"],
        "subject": note_data["subject"],
        "tags": note_data["tags"],
        "created_at": str(note_data.get("created_at"))
    }

