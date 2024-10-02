from fastapi import APIRouter
from .. import schemas, oauth2
from sqlalchemy.orm import Session
from fastapi import Depends
from ..database import get_db
from typing import List
from ..repository import book
from typing import Annotated

router = APIRouter(
    prefix='/book',
    tags=['Books']
)

#fetching all records
@router.get('/',status_code=200, response_model=List[schemas.ShowBook])
def all(current_user: Annotated[schemas.User, Depends(oauth2.get_current_user)],db: Session=Depends(get_db)):
    return book.all(db)

@router.post('/', response_model=schemas.BookCreate, status_code=201)
def create(current_user: Annotated[schemas.User, Depends(oauth2.get_current_user)],request: schemas.Book, db: Session=Depends(get_db)):
    return book.create(request, db)

#fetching first record with corresponding id
@router.get('/{id}', response_model=schemas.ShowBook)
def show(current_user: Annotated[schemas.User, Depends(oauth2.get_current_user)],id: int,db: Session=(Depends(get_db))):
    return book.show(id, db)

@router.delete('/{id}')
def destroy(current_user: Annotated[schemas.User, Depends(oauth2.get_current_user)],id: int, db: Session=(Depends(get_db))):
    return book.destroy(id, db)

#partial update
@router.put('/{id}')
def update(current_user: Annotated[schemas.User, Depends(oauth2.get_current_user)],id: int, request: schemas.Book, db: Session=(Depends(get_db))):
    return book.update(id, db)
    
#full update   
@router.put('/update/{id}')
def full_update(current_user: Annotated[schemas.User, Depends(oauth2.get_current_user)],id: int, request: schemas.Book, db: Session=(Depends(get_db))):
    return book.full_update(id, db)