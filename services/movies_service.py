from  fastapi import  HTTPException, status
from sqlalchemy.orm import Session
import models, schema



def get_movies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Movie).offset(skip).limit(limit).all()

def create_movie(db: Session, movie: schema.MovieCreate, user_id: int = None):
    db_movie = models.Movie(
        **movie.model_dump(), 
        user_id=user_id
        )
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def get_single_movie(db: Session,  id: int = None):
    movie   =  db.query(models.Movie).filter(models.Movie.id == id).first()

    if  not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with id {id} not found")
    return movie

def update_movie(db: Session, movie_id: int, movie_payload: schema.Movie):
    movie = get_movies(db, movie_id)
    if not movie:
        return None
    
    movie_payload_dict = movie_payload.model_dump(exclude_unset=True)

    for key, value in movie_payload_dict.items():
        setattr(movie, key, value)

    db.add(movie)
    db.commit()
    db.refresh(movie)

    return movie