from app.base.config import settings
from app.base.db import SessionLocal, engine
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, Query, Response
from fastapi_cache.decorator import cache
from sqlalchemy import text

router = APIRouter()


@router.get("/ping")
async def healthcheck():
    return {"ping": "pong"}


@router.get("/get_db_version")
async def get_db_status():
    db = SessionLocal()
    version = db.execute(text("SELECT VERSION()")).fetchone()

    return {"db_version": {version[0]}}
