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

origins = [
    # local
    # sml
    "http://localhost:3000",
    "http://localhost:80",
    "http://localhost",
    # smc
    # público
    "http://localhost:3001",
    # autoridades
    "http://localhost:3002",
    "http://localhost:443",
    # smr
    "http://localhost:3003",

    # int2
    # sml
    "https://cdn-fch-int-sml-endpoint.azureedge.net",
    "http://20.10.169.219:3000",
    "http://20.10.169.219:80",
    "http://20.10.169.219",
    # smc
    # público
    "https://cdn-fch-int-endpoint.azureedge.net",
    "http://172.177.206.225:3000",
    "http://172.177.206.225:80",
    "http://172.177.206.225",
    # autoridades
    "https://cdn-fch-int-aut-endpoint.azureedge.net",
    "http://172.177.206.225:3001",
    "http://172.177.206.225:443",
    # smr
    "https://cdn-fch-int-smr-endpoint.azureedge.net",

    # alpha2
    # sml
    "https://cdn-alpha-sml-endpoint.azureedge.net",
    "http://20.119.249.21:3000",
    "http://20.119.249.21:80",
    "http://20.119.249.21",
    # smc
    # público
    "https://cdn-alpha-endpoint.azureedge.net",
    "http://20.22.204.132:3000",
    "http://20.22.204.132:80",
    "http://20.22.204.132",
    # autoridades
    "https://cdn-alpha-aut-endpoint.azureedge.net",
    "http://20.22.204.132:3001",
    "http://20.22.204.132:443",
    # smr
    "https://cdn-alpha-smr-endpoint.azureedge.net",

    # preprod
    # sml
    "https://cdn-preprod-sml-endpoint.azureedge.net",
    # smc
    # público
    "https://cdn-preprod-endpoint.azureedge.net",
    # autoridades
    "https://cdn-preprod-aut-endpoint.azureedge.net",
    # smr
    "https://cdn-preprod-smr-endpoint.azureedge.net",

    # prod
    # sml
    "https://cdn-prod-sml-endpoint.azureedge.net",
    # smc
    # público
    "https://cdn-prod-endpoint.azureedge.net",
    # autoridades
    "https://cdn-prod-aut-endpoint.azureedge.net",
    # smr
    "https://cdn-prod-smr-endpoint.azureedge.net"]


async def init_db(app: FastAPI):
    register_tortoise(
        app,
        db_url="postgres://"+POSTGRES_USER+":"+POSTGRES_PASSWORD+"@"+DATABASE_HOST+":"+DATABASE_PORT+"/"+POSTGRES_DB,
        #db_url='postgres://{}:{}@{}:{}/{}'.format(POSTGRES_USER, POSTGRES_PASSWORD, DATABASE_HOST, DATABASE_PORT, POSTGRES_DB),
        modules={"models": ["app.models.ticketModel", "app.models.ticketLogModel", "app.models.ticketCommentModel", "app.models.autorizathionRequestModel"]},
        generate_schemas=False,
        add_exception_handlers=True
    )
