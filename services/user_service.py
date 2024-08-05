from sqlalchemy.orm import Session
import models, schema
from authentication import hash_password

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schema.UserCreate):
    
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.hashed_password)
    )
    # db_user = models.User()
    # db_user.email = user.email
    # db_user.hashed_password = hash_password(user.hashed_password)
    # db_user.username = user.username

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user