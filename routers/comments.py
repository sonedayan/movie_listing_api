from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import schema
from services import comments_service, movies_service
from database import get_db
from authentication import get_current_user
from logger import logger

comment_router = APIRouter()

@comment_router.post("/movies/{movie_id}/comments", response_model=schema.Comment)
def create_comment(movie_id:int, comment: schema.CommentCreate, db: Session = Depends(get_db), user: schema.User = Depends(get_current_user)):
    logger.info("Creating comment...")
    movie = movies_service.get_single_movie(db, movie_id)
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    logger.info("Comment created successfully...")
    return comments_service.create_comment(db=db, comment=comment, user_id=user.id, movie_id=movie_id)

@comment_router.get("/movies/{movie_id}/comments", response_model=List[schema.Comment])
def read_comments(movie_id: int, db: Session = Depends(get_db)):
    movie = movies_service.get_single_movie(db, movie_id)
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    
    return comments_service.get_comments(db, movie_id=movie_id)


@comment_router.get("/comments/{comment_id}", response_model=schema.Comment)
def get_single_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = comments_service.get_comment(db=db, comment_id=comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment


@comment_router.post("/movies/{movie_id}/comments/{parent_id}/reply", response_model=schema.Comment, status_code=status.HTTP_201_CREATED)
def reply_to_comment(movie_id: int, parent_id: int, comment: schema.CommentCreate, db: Session = Depends(get_db), user: schema.User = Depends(get_current_user)):
    movie = movies_service.get_single_movie(db, movie_id=movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    parent_comment = comments_service.get_comment(db=db, comment_id=parent_id)
    if not parent_comment:
        raise HTTPException(status_code=404, detail="Parent comment not found")

    return comments_service.create_comment(db=db, comment=comment, user_id=user.id, movie_id=movie_id, parent_id=parent_id)

@comment_router.put("/comments/{comment_id}", response_model=schema.Comment)
def update_comment(comment_id: int, updated_comment: schema.Comment, db: Session = Depends(get_db), user: schema.User = Depends(get_current_user)):
    comment = comments_service.get_comment(db=db, comment_id=comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    if comment.user_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this comment")

    return comments_service.update_comment(db=db, comment_id=comment_id, new_content=updated_comment.content, user_id=user.id)


@comment_router.delete("/comments/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(comment_id: int, db: Session = Depends(get_db), user: schema.User = Depends(get_current_user)):
    comment = comments_service.get_comment(db=db, comment_id=comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    if comment.user_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this comment")

    success = comments_service.delete_comment(db=db, comment_id=comment_id, user_id=user.id)
    if not success:
        raise HTTPException(status_code=400, detail="Failed to delete comment")

    return {"detail": "Comment deleted successfully"}
    
