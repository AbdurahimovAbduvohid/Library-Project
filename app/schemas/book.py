from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class BookBase(BaseModel):
    title: str
    author: str
    publication_year: int


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    views: int

    class Config:
        orm_mode = True


class CommentBase(BaseModel):
    text: str


class CommentCreate(CommentBase):
    book_id: int


class Comment(CommentBase):
    id: int
    created_at: datetime
    book_id: int
    user_id: int

    class Config:
        orm_mode = True


class LoanBase(BaseModel):
    book_id: int


class LoanCreate(LoanBase):
    pass


class Loan(LoanBase):
    id: int
    user_id: int
    loan_date: datetime
    return_date: Optional[datetime]
    is_returned: bool

    class Config:
        orm_mode = True
