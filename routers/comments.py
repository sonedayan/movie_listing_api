from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import schema
from services import comments_service
from database import get_db

comment_router = APIRouter(
    prefix="/comments",
    tags=["comments"]
)

@comment_router.post("/", response_model=schema.Comment)
def create_comment(comment: schema.CommentCreate, db: Session = Depends(get_db)):
    return comments_service.create_comment(db=db, comment=comment)

@comment_router.get("/{movie_id}", response_model=List[schema.Comment])
def read_comments(movie_id: int, db: Session = Depends(get_db)):
    comments = comments_service.get_comments(db, movie_id=movie_id)
    return comments
