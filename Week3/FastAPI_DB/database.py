from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# .env file load பண்ணு — இது FIRST இருக்கணும்!
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Debug — None வருதான்னு check பண்ண
print(f"DATABASE_URL = {DATABASE_URL}")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()