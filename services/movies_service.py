from sqlalchemy.orm import Session
import models, schema



def get_movies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Movie).offset(skip).limit(limit).all()

def create_movie(db: Session, movie: schema.MovieCreate, user_id: int):
    db_movie = models.Movie(**movie.dict(), user_id=user_id)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie