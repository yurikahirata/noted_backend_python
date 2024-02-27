from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import dotenv_values
from pymongo import MongoClient
from notes_routes import router as notes_router

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