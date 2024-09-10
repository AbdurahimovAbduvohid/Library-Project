import uvicorn
from fastapi import FastAPI
from app.routes import book, user
from app.models import book as book_model, user as user_model
from config.database import engine

book_model.Base.metadata.create_all(bind=engine)
user_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(book.router, prefix="/api")
app.include_router(user.router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
