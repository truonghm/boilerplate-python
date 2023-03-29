# import databases
from app.base.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# import pymysql
# import cryptography

user = settings.MYSQL_USER
password = settings.MYSQL_PWD
host = settings.MYSQL_HOST
port = settings.MYSQL_PORT
database = settings.MYSQL_DB

connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8"
# print(connection_string)

engine = create_engine(connection_string, max_identifier_length=30, pool_size=2, max_overflow=0)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

Base.metadata.create_all(engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        # db.rollback()
        yield db
    finally:
        db.close()
