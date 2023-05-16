from tortoise.contrib.fastapi import register_tortoise
#from tortoise import Tortoise
from fastapi import FastAPI
#from pydantic import BaseSettings
#from functools import lru_cache
from dotenv import load_dotenv
import os

# Loading environment variables from .env
load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")


async def init_db(app: FastAPI):
    register_tortoise(
        app,
        db_url="postgres://"+POSTGRES_USER+":"+POSTGRES_PASSWORD+"@"+DATABASE_HOST+":"+DATABASE_PORT+"/"+POSTGRES_DB,
        #db_url='postgres://{}:{}@{}:{}/{}'.format(POSTGRES_USER, POSTGRES_PASSWORD, DATABASE_HOST, DATABASE_PORT, POSTGRES_DB),
        modules={"models": ["app.models.ticketModel", "app.models.ticketLogModel", "app.models.ticketCommentModel", "app.models.autorizathionRequestModel"]},
        generate_schemas=True,
        add_exception_handlers=True
    )
