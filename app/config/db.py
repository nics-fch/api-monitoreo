from tortoise import Tortoise
import os

# Environment variable
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

async def init_db():
    await Tortoise.init(
        db_url="postgres://"+ POSTGRES_USER+":"+POSTGRES_PASSWORD+"@"+DATABASE_HOST+":"+DATABASE_PORT+"/"+POSTGRES_DB,
        modules={"models": ["models"]},
    )
    await Tortoise.generate_schemas()

async def close_db():
    await Tortoise.close_connections()
