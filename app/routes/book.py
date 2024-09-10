from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.book import Book, BookCreate, Comment, CommentCreate, Loan, LoanCreate
from app.services import book as book_service
from app.dependencies import get_db, get_current_user
from app.schemas.user import User

router = APIRouter()


@router.post("/books/", response_model=List[Book])
def create_new_book(book: BookCreate, user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="User not found")
    return book_service.create_book(db=db, book=book, user_id=user_id)


@router.get("/books/", response_model=List[Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return book_service.get_books(db, skip=skip, limit=limit)


@router.get("/books/{book_id}", response_model=Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = book_service.get_book(db, book_id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    updated_book = book_service.update_book(db, book_id=book_id, book=book)
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book


@router.delete("/books/{book_id}", response_model=Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    deleted_book = book_service.delete_book(db, book_id=book_id)
    if deleted_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return deleted_book


@router.post("/books/{book_id}/comments/", response_model=Comment)
def create_comment(
        book_id: int, comment: CommentCreate, db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    return book_service.create_comment(db=db, comment=comment, user_id=current_user.id)


@router.post("/books/{book_id}/loans/", response_model=Loan)
def create_loan(
        book_id: int, db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    return book_service.create_loan(db=db, loan=LoanCreate(book_id=book_id), user_id=current_user.id)


@router.post("/loans/{loan_id}/return", response_model=Loan)
def return_book(loan_id: int, db: Session = Depends(get_db)):
    returned_loan = book_service.return_book(db=db, loan_id=loan_id)
    if returned_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return returned_loan


@router.get("/books/most-read/", response_model=List[Book])
def read_most_read_books(limit: int = 10, db: Session = Depends(get_db)):
    return book_service.get_most_read_books(db=db, limit=limit)
