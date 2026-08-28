import sys
import os 

import pymongo
import certifi
ca = certifi.where()

from dotenv import load_dotenv
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.pipeline.training_pipeline import TrainingPipeline

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import RedirectResponse

import pandas as pd

from networksecurity.utils.main_utils.utils import load_object

load_dotenv()
MONGO_DB_URL = os.getenv("MONGA_ATLAS_URI")

client = pymongo.MongoClient(MONGO_DB_URL,tlsCAFFile=ca)

from networksecurity.constants.training_pipeline import DATA_INGESTION_COLLECTION_NAME
from networksecurity.constants.training_pipeline import DATA_INGESTION_DATABASE_NAME

database = client(DATA_INGESTION_DATABASE_NAME)
collection = client(DATA_INGESTION_DATABASE_NAME)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def train_route():
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()

        return Response("Training is Successful")
    except Exception as e:
        raise NetworkSecurityException(e,sys)