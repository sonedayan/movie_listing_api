from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from services import user_service
from database import get_db

import schema

user_router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@user_router.post("/", response_model=schema.User)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = user_service.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_service.create_user(db=db, user=user)

@user_router.get("/{user_id}", response_model=schema.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_service.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
