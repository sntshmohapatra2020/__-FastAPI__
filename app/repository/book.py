from fastapi import APIRouter
from .. import schemas, models
from sqlalchemy.orm import Session
from fastapi import Depends
from ..database import get_db
from sqlalchemy.orm import Session
from fastapi import status, HTTPException

def full_update(id:int, request: schemas.Book, db: Session=Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'book with id {id} not found')
    else:
        book.title = request.title
        book.body = request.body
        book.user_id = request.user_id
        db.commit()
        return 'successfully updated'
    
def update(id, request: schemas.Book, db: Session=Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'book with {id} not found')
    else:
        if request.title:
            book.title = request.title
        if request.body:
            book.body = request.body
        db.commit()
        return 'successfully updated'
    
def destroy(id, db: Session=Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'book with {id} not found')
    else:
        book.delete(synchronize_session=False)
        db.commit()
        return 'successfully deleted'
    
def show(id, db: Session=Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'book with {id} not found')
    return book

def create(request: schemas.Book,db:Session=Depends(get_db)):
    new_book = models.Book(title=request.title, body=request.body,user_id=request.user_id)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def all(db:Session=Depends(get_db)):
    books = db.query(models.Book).all()
    return books