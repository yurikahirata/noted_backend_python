import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Collection(BaseModel):
    username: str = Field(...)
    collectionName: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "yurika",
                "collectionName": "unsorted"
            }
        }

class Note(BaseModel):
    username: str = Field(...)
    content: str = Field(...)
    collection: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "yurika",
                "content": "test note",
                "collection": "unsorted"
            }
        }

class User(BaseModel):
    username: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "yurika",
                "password": "h3bAhbje4sUMe89332nXyajsS44"
            }
        }


class UpdateNote(BaseModel):
    content: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "content": "new and updated note!"
            }
        }


class GetNotesByUsernameAndCollection(BaseModel):
    username: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "yurika"
            }
        }


class EditNotesByUsernameAndCollection(BaseModel):
    username: str = Field(...)
    collection: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "yurika",
                "collection": "new collection"
            }
        }