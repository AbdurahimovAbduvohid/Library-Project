from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    name: str
    login: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    created_at: datetime
    is_active: bool

    class Config:
        orm_mode = True


class UserInDB(User):
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str = None
