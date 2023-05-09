from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from .routes.monitorRoute import router
from dotenv import load_dotenv

# Loading environment variables from .env
load_dotenv()

# The main object is created
app = FastAPI(
    title="API Monitoreo",
    version="v1.0",
    description="SMC - API Monitoreo DP",
)

# By default we send them to the docs
@app.get("/")
async def docs_redirect():
    return RedirectResponse(url='/docs')

#We include all our routes
app.include_router(router)
