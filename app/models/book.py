from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from config.database import Base
from datetime import datetime


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    publication_year = Column(Integer)
    views = Column(Integer, default=0)

    comments = relationship("Comment", back_populates="book")
    loans = relationship("Loan", back_populates="book")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    book_id = Column(Integer, ForeignKey("books.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    book = relationship("Book", back_populates="comments")
    user = relationship("User", back_populates="comments")


class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    loan_date = Column(DateTime, default=datetime)
    return_date = Column(DateTime)
    is_returned = Column(Boolean, default=False)

    book = relationship("Book", back_populates="loans")
    user = relationship("User", back_populates="loans")
