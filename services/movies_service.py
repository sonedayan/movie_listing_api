from  fastapi import  HTTPException, status
from sqlalchemy.orm import Session
import models, schema



def get_movies(db: Session, user_id: int = None, offset: int = 0, limit: int = 10):
    return db.query(models.Movie).filter(models.Movie.user_id == user_id).offset(offset).limit(limit).all()

def create_movie(db: Session, movie: schema.MovieCreate, user_id: int = None):
    db_movie = models.Movie(
        **movie.model_dump(), 
        user_id=user_id
        )
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def get_single_movie(db: Session,  id: int):
    return db.query(models.Movie).filter(models.Movie.id == id).first()


def update_movie(db: Session, movie_id: int, movie: schema.MovieUpdate, user_id: int = None):
    db_movie = get_single_movie(db, movie_id)
    if db_movie.user_id == user_id:
        for key, value in movie.model_dump().items():
            setattr(db_movie, key, value)
        db.commit()
        db.refresh(db_movie)
        return db_movie
    return None
    # movie = get_single_movie(db, movie_id)
    # if not movie:
    #     return None
    
    # movie_payload_dict = movie_payload.model_dump(exclude_unset=True)

    # for key, value in movie_payload_dict.items():
    #     setattr(movie, key, value)

    # db.add(movie)
    # db.commit()
    # db.refresh(movie)

    # return movie

def delete_movie(db: Session, movie_id: int, user_id: int):
    db_movie = get_single_movie(db, movie_id)
    if db_movie.user_id == user_id:
        db.delete(db_movie)
        db.commit()
        return True
    return False

    # movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    # if movie:
    #     db.delete(movie)
    #     db.commit()
    #     return True
    # return False