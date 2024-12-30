from typing import List
from fastapi import APIRouter,Depends,status,Response,HTTPException
from .. import schemas,models,database,oauth2
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter( prefix="/blog",tags=["blogs"]  )
get_db = database.get_db

@router.get("/",response_model=List[schemas.ShowBlog])
def all_blog(db:Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.post("/",status_code=status.HTTP_201_CREATED)
def create_blog(request:schemas.Blog,db:Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
   return blog.create(request,db)


@router.put("/{id",status_code=status.HTTP_202_ACCEPTED)
def update_blog(id,request:schemas.Blog,db:Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id,response:Response,db:Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(id,db)

@router.get("/{id}",status_code=200,response_model=schemas.ShowBlog)
def single_blog(id,response:Response,db:Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.single_blog(id,db)