from fastapi import APIRouter, Body, Request, status
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId

from notes_models import Note, GetNotesByUsernameAndCollection, UpdateNote, EditNotesByUsernameAndCollection

router = APIRouter()

@router.post("/", response_description="Create a new note", status_code=status.HTTP_200_OK)
def create_note(request: Request, note: Note = Body(...), ):
    note = jsonable_encoder(note)
    request.app.database["notes"].insert_one(note)

    return "New note created!"


@router.patch("/{id}", response_description="Update a note", status_code=status.HTTP_200_OK)
def update_note(id: str, request: Request, note: UpdateNote = Body(...)):
    note = jsonable_encoder(note)
    print(note)
    request.app.database["notes"].update_one(
        { "_id": ObjectId(id) }, { "$set": note }
    )

    return "Updated note!"


@router.delete("/{id}", response_description="Delete a note", status_code=status.HTTP_200_OK)
def delete_note(id: str, request: Request):
    condition = {"_id": ObjectId(id)}
    request.app.database["notes"].delete_one(condition)

    return "Deleted note!"


@router.post("/username/{collection}", response_description="Get notes by username and collection", status_code=status.HTTP_200_OK)
def get_notes_by_username_collection(request: Request, collection: str, username: GetNotesByUsernameAndCollection = Body(...) ):
    checkUsername = getattr(username, "username")
    
    notes = list(request.app.database["notes"].find({"username" : checkUsername, "collection" : collection}, {"_id": 0} ))
    return notes

@router.patch("/username/{collection}", response_description="Edit notes by username and collection", status_code=status.HTTP_200_OK)
def edit_notes_by_username_collection(request: Request, collection: str, body: EditNotesByUsernameAndCollection = Body(...) ):
    checkUsername = getattr(body, "username")
    updateCollection = getattr(body, "collection")
    condition = { "username": checkUsername, "collection": collection };
    updateTo = { "$set": {"collection": updateCollection}};

    request.app.database["notes"].update_many(condition, updateTo )
    return "notes updated!"


@router.delete("/{username}/{collection}", response_description="Delete notes by username and collection", status_code=status.HTTP_200_OK)
def edit_notes_by_username_collection(request: Request, username: str, collection: str):
    condition = {"username" : username, "collection": collection}

    request.app.database["notes"].delete_many(condition)
    return "notes deleted!"