from fastapi import APIRouter, Body, Request, status, Response
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId

from collections_models import Collection, EditCollection, Username

router = APIRouter()

@router.post("/", response_description="Create a new collection", status_code=status.HTTP_200_OK)
def create_collection(request: Request, collection: Collection = Body(...)):
    collection = jsonable_encoder(collection)
    request.app.database["collections"].insert_one(collection)
    return("new note created!")


@router.delete("/{id}", response_description="Delete a collection", status_code=status.HTTP_200_OK)
def delete_collection(id: str, request: Request):
    condition = {"_id": ObjectId(id)}
    request.app.database["collections"].delete_one(condition)

    return "Deleted collection!"


@router.patch("/{id}", response_description="Edit collection", status_code=status.HTTP_200_OK)
def edit_collection(request: Request, id: str, entry: EditCollection = Body(...) ):
    entry = jsonable_encoder(entry)
    condition = { "_id": ObjectId(id) };
    updateTo = { "$set": entry};

    request.app.database["collections"].update_one(condition, updateTo)
    return "Collection updated!"


@router.post("/username", response_description="Get all collections by username", status_code=status.HTTP_200_OK)
def get_collections_by_username(request: Request, username: Username = Body(...)):
    checkUsername = getattr(username, "username")
    collections = list(request.app.database["collections"].find({"username": checkUsername}, {"_id": 0}))
    return collections