from typing import List
from fastapi import APIRouter,Depends,status,Response,HTTPException
from .. import schemas,models,database
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..repository import user

router = APIRouter(tags=["users"])
get_db = database.get_db




@router.post("/user",response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session = Depends(get_db)):
   return user.create_user(request,db)

@router.get("/user/{id}",response_model=schemas.ShowUser)
def get_user(id:int,db:Session = Depends(get_db)):
   return user.get_user(id,db)