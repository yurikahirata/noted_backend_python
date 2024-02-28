from pydantic import BaseModel, Field

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