from sqlalchemy.orm import Session
import models, schema


def get_comments(db: Session, movie_id: int):
    return db.query(models.Comment).filter(models.Comment.movie_id == movie_id).all()

def create_comment(db: Session, comment: schema.CommentCreate):
    db_comment = models.Comment(**comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment