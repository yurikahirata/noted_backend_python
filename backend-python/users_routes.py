from fastapi import APIRouter, Body, Request, status, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from bson.objectid import ObjectId
import bcrypt
import requests
import json

saltRounds = 10

from users_models import User, Username

router = APIRouter()

@router.post("/username", response_description="Get by username")
def check_user(request: Request, username: Username = Body(...)):
    username = getattr(username, "username")
    user = request.app.database["users"].find_one({"username": username}, {"_id":0})
    if isinstance(user, dict):
        user_bytes = json.dumps(user).encode('utf-8')
        return Response(content=user_bytes)
    return False


@router.post("/", response_description="Create a new user", status_code=status.HTTP_200_OK)
def create_user(request: Request, response: Response, user: User = Body(...)):
    user = jsonable_encoder(user)

    res = requests.post("http://127.0.0.1:8000/users/username", json={"username":user["username"]})
    if (res.text != "false"):
      response.status_code = status.HTTP_400_BAD_REQUEST
      return "Username taken"
    
    salt = bcrypt.gensalt(saltRounds)
    password = user["password"]
    bytes = password.encode('utf-8')
    hashedPassword = bcrypt.hashpw(bytes, salt)
    hashedPassword = hashedPassword.decode('utf-8')

    newUser = {"username": user["username"], "hashedPassword": hashedPassword}

    insertedId = request.app.database["users"].insert_one(newUser)
    insertedId = insertedId.inserted_id

    result = request.app.database["users"].find_one({"_id": ObjectId(insertedId)})
    result["_id"] = str(result["_id"])

    return result

@router.post("/session", response_description="Authenticate a user", status_code=status.HTTP_200_OK)
def authenticate_user(request: Request, response: Response, user: User = Body(...)):
    user = jsonable_encoder(user)

    res = requests.post("http://127.0.0.1:8000/users/username", json={"username":user["username"]})

    if (res.text == "false"):
      response.status_code = status.HTTP_400_BAD_REQUEST
      return "Incorrect username"
    
    res = json.loads(res.content.decode('utf-8'))
    
    password = user["password"]
    bytes = password.encode('utf-8')
    result = bcrypt.checkpw(bytes, res["hashedPassword"].encode('utf-8'))

    if (result != True):
      response.status_code = status.HTTP_400_BAD_REQUEST
      return "Incorrect password"
    
    return "User authenticated!"

