from fastapi import APIRouter, status, HTTPException
from .. import schemas, models, token
from sqlalchemy.orm import Session
from fastapi import Depends
from ..database import get_db
from typing import Annotated
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    prefix='/login',
    tags=["login"]
)

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")
def verify(hashed_password, plain_password):
    return pwd_cxt.verify(plain_password, hashed_password)

@router.post('/')
def login(request: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with username {request.username} not found')
    if not verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Incorrect Password')
    access_token = token.create_access_token(data={"sub": user.email})
    return schemas.Token(access_token=access_token, token_type="bearer")