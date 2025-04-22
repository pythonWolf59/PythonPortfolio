from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    full_name = Column(String)
    hashed_password = Column(String)  # Store hashed passwords for security
    