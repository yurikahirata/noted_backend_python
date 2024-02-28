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

class EditCollection(BaseModel):
    collectionName: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "collectionName": "unsorted"
            }
        }

class Username(BaseModel):
    username: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "yurika"
            }
        }