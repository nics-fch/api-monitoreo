from fastapi import FastAPI
#from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise
from .routes.monitorRoute import router
#from dotenv import load_dotenv
from .config.db import init_db,origins
from fastapi.middleware.cors import CORSMiddleware

# Loading environment variables from .env
#load_dotenv()

# The main object is created
app = FastAPI(
    title="API Monitoreo",
    version="v1.0",
    description="SMC - API Monitoreo DP",
)

# Configure the allowed origins for CORS
origins = [
    "*",
]

# Add CORS middleware to your app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])


@app.on_event("startup")
async def startup_event():
    await init_db(app)

@app.on_event("shutdown")
async def shutdown_event():
    await Tortoise.close_connections()


# By default we send them to the docs
"""
@app.get("/")
async def docs_redirect():
    return RedirectResponse(url='/docs')
"""

#We include all our routes
app.include_router(router)