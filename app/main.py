from fastapi import FastAPI
from app.routes import items_router
from .database import init_db

app = FastAPI()

app.include_router(items_router)

@app.on_event("startup")
async def startup_event():
    await init_db()
