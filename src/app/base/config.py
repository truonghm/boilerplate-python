import os
from pathlib import Path


class Settings(object):
    ROOT_DIR = Path(__file__).parent.parent.parent.parent
    API_HOST_PORT = int(os.getenv("API_HOST_PORT", 8000))
    API_HOST_DOMAIN = os.getenv("API_HOST_DOMAIN", "'0.0.0.0'")
    RELOAD_CODE = True
    NUMBER_OF_WORKER = int(os.getenv("NUMBER_OF_WORKER", 2))
    NUMBER_OF_API_INSTANCES = int(os.getenv("NUMBER_OF_API_INSTANCES", 2))
    NUMBER_OF_DB_CONNECT = (NUMBER_OF_API_INSTANCES + NUMBER_OF_WORKER) * 4
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_USER = os.getenv("MYSQL_USER", "admin")
    MYSQL_PWD = os.getenv("MYSQL_PWD", "admin")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
    MYSQL_DB = os.getenv("MYSQL_DB", "st")


settings = Settings()
