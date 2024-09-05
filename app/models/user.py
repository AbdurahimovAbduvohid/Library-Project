from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from config.database import Base
from datetime import datetime



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    login = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime)
    is_active = Column(Boolean, default=True)

    comments = relationship("Comment", back_populates="user")
    loans = relationship("Loan", back_populates="user")
