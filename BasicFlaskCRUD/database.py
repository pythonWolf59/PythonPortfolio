from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#SQLite Database URL
DATABASE_URL = "sqlite:///users.db"

# Create a new SQLite database (or connect to an existing one)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()