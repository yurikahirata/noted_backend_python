from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import dotenv_values
from pymongo import MongoClient
from notes_routes import router as notes_router
from users_routes import router as users_router
from collections_routes import router as collections_router

config = dotenv_values(".env")

@asynccontextmanager
async def lifespan(app: FastAPI):
  #startup
  app.mongodb_client = MongoClient(config["ATLAS_URI"])
  app.database = app.mongodb_client[config["DB_NAME"]]
  print("Connected to the MongoDB database!!")

  yield

  #shutdown
  app.mongodb_client.close()

app = FastAPI(lifespan=lifespan)

app.include_router(notes_router, tags=["notes"], prefix="/notes")
app.include_router(users_router, tags=["users"], prefix="/users")
app.include_router(collections_router, tags=["collections"], prefix="/collections")