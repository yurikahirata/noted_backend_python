from pydantic import BaseModel, Field

class User(BaseModel):
    username: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "yurika",
                "password": "1234"
            }
        }


class Username(BaseModel):
    username: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "yurika",
            }
        }