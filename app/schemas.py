from pydantic import BaseModel
from typing import List
class Book(BaseModel):
    title: str
    body: str
    user_id :int
    class Config:
        orm_mode = True

class BookCreate(Book):
    id: int
    class Config:
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str   
    class Config:
        orm_mode = True
        
class ShowUser(BaseModel):
    name: str
    email: str
    books: List[Book] = []
    class Config:
        orm_mode = True   

class ShowBook(BaseModel):
    title: str
    body: str
    creator : User
    class Config:
        orm_mode = True 
        
class Login(BaseModel):
    username: str
    password: str
    class Config:
        orm_mode = True  

class Token(BaseModel):
    access_token: str
    token_type: str
    class Config:
        orm_mode = True


class TokenData(BaseModel):
    email: str | None = None
    class Config:
        orm_mode = True