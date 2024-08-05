from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from services import user_service
from database import get_db
from authentication import pwd_context, authenticate_user, create_access_token, get_current_user

import schema

user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@user_router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    
    return user_service.create_user(db=db, user=user)

@user_router.get("/{user_id}", response_model=schema.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_service.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user

@user_router.post("/signup", response_model=schema.User)

def signup(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = user_service.get_user_by_email(db, user = user.email)
    hashed_password = pwd_context.hash(user.password)
    if db_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")
    return user_service.create_user(db=db, user=user, hashed_password=hashed_password)

@user_router.post("/login")
def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.email, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password", headers={"WWW-Authenticate": "Bearer"})
    #access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}