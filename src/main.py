import sys
import time

import aioredis
import uvicorn

# load_dotenv()
# try:
#     if sys.argv[1] == "local":
#         settings.MYSQL_HOST = "localhost"
# except IndexError:
#     pass
from app.base.config import settings
from app.base.db import SessionLocal, engine
from app.main_routers import add_all_routers
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from uvicorn.config import LOGGING_CONFIG

app = FastAPI(
    title="Streamlit Backend APIs",
    description="Streamlit Backend APIs",
    version="0.0.1",
    docs_url="/documentation",
    redoc_url="/redoc",
)
add_all_routers(app)


@app.get("/")
async def read_main():
    return {"msg": "Streamlit Backend APIs"}


if __name__ == "__main__":
    LOGGING_CONFIG["formatters"]["access"][
        "fmt"
    ] = '%(asctime)s %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s'
    LOGGING_CONFIG["formatters"]["access"]["datefmt"] = "%Y-%m-%d %H:%M:%S"

    uvicorn.run(
        "main:app",
        host=settings.API_HOST_DOMAIN,
        port=settings.API_HOST_PORT,
        reload=settings.RELOAD_CODE,
        workers=settings.NUMBER_OF_WORKER,
    )
