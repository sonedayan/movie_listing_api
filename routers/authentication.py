from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from services import auth_service
from database import get_db
from authentication import pwd_context, authenticate_user, create_access_token, get_current_user
from logger import logger


import schema

auth_router = APIRouter()

# @auth_router.post("/", status_code=status.HTTP_201_CREATED)
# def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    
#     return auth_service.create_user(db=db, user=user)

# @auth_router.get("/{user_id}", response_model=schema.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = auth_service.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
#     return db_user

@auth_router.post("/register", response_model=schema.User, status_code=status.HTTP_201_CREATED)

def signup(user: schema.UserCreate, db: Session = Depends(get_db)):
    logger.info(f"Creating user...")
    db_user = auth_service.get_user_by_username(db, username = user.username)
    hashed_password = pwd_context.hash(user.password)
    if db_user:
        logger.warning(f"User with {user.username} already exists.")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username already registered")
    logger.info(f"User {user.username} created successfully.")

    return auth_service.create_user(db=db, user=user, hashed_password=hashed_password)

@auth_router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Incorrect username or password", 
            headers={"WWW-Authenticate": "Bearer"}
            )
    #access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}