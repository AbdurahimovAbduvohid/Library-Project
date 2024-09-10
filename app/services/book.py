from sqlalchemy.orm import Session
from app.models.book import Book, Comment, Loan
from app.schemas.book import BookCreate, CommentCreate, LoanCreate
from fastapi import HTTPException
from datetime import datetime, timedelta


def get_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    book.views += 1
    db.commit()
    return book


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()


def create_book(db: Session, book: BookCreate, user_id: int):
    db_book = Book(title=book.title, author=book.author, publication_year=book.publication_year, user_id=user_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def update_book(db: Session, book_id: int, book: BookCreate):
    db_book = get_book(db, book_id)
    for key, value in book.dict().items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int):
    db_book = get_book(db, book_id)
    db.delete(db_book)
    db.commit()
    return db_book


def create_comment(db: Session, comment: CommentCreate, user_id: int):
    db_comment = Comment(**comment.dict(), user_id=user_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def create_loan(db: Session, loan: LoanCreate, user_id: int):
    db_loan = Loan(**loan.dict(), user_id=user_id, loan_date=datetime)
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan


def return_book(db: Session, loan_id: int):
    loan = db.query(Loan).filter(Loan.id == loan_id).first()
    if loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    if loan.is_returned:
        raise HTTPException(status_code=400, detail="Book already returned")
    loan.return_date = datetime
    loan.is_returned = True
    db.commit()
    db.refresh(loan)
    return loan


def get_most_read_books(db: Session, limit: int = 10):
    return db.query(Book).order_by(Book.views.desc()).limit(limit).all()
