from sqlalchemy.orm import Session
import models, schema


def get_comments(db: Session, movie_id: int):
    return db.query(models.Comment).filter(models.Comment.movie_id == movie_id).all()

def create_comment(db: Session, comment: schema.CommentCreate, user_id: int, movie_id: int):
    db_comment = models.Comment(
        **comment.model_dump(), user_id=user_id, movie_id=movie_id
        )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comments_by_movie(db: Session, movie_id: int):
    return db.query(models.Comment).filter(models.Comment.movie_id == movie_id).all()

def get_comment(db: Session, comment_id: int):
    return db.query(models.Comment).filter(models.Comment.id == comment_id).first()

def update_comment(db: Session, comment_id: int, new_content: str, user_id: int):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id, models.Comment.user_id == user_id).first()
    if db_comment:
        db_comment.content = new_content
        db.commit()
        db.refresh(db_comment)
    return db_comment

def delete_comment(db: Session, comment_id: int, user_id: int):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id, models.Comment.user_id == user_id).first()
    if db_comment:
        db.delete(db_comment)
        db.commit()
        return True
    return False