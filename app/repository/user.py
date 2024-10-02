from passlib.context import CryptContext
from .. import models
from .. import schemas
from sqlalchemy.orm import Session
from fastapi import Depends
from ..database import get_db
from fastapi import status, HTTPException

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(request: schemas.User, db:Session=Depends(get_db)):
    hashed_password = pwd_cxt.hash(request.password) 
    new_user = models.User(name=request.name, email=request.email, password=hashed_password)    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id: int, db: Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with id {id} not found')
    return user