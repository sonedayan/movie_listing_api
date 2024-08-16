from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services import movies_service
import schema as schema
from authentication import get_current_user
from logger import logger

movie_router = APIRouter()

@movie_router.get("/movies/", status_code=status.HTTP_200_OK)
def get_movies(db: Session = Depends(get_db), user: schema.User = Depends(get_current_user), offset: int = 0, limit: int = 10):
    logger.info(f'Getting movies for {user.username} ...')
    movies = movies_service.get_movies(db, user_id=user.id, offset=offset, limit=limit)
    logger.info(f"Movies gotten for {user.username}")
    return {
        "message": "Movies retrieved successfully",
        "data": movies
    }

@movie_router.post("/movies/", status_code=status.HTTP_201_CREATED)
def create_movie(payload: schema.MovieCreate, user: schema.User = Depends(get_current_user), db: Session = Depends(get_db)):
    logger.info("Creating a new movie: %s", movie.title)
    movie = movies_service.create_movie(db=db, movie=payload, user_id=user.id)
    logger.info("Movie created successfully with ID: %d", movie.id)
    return {
        "message": "Movie created successfully",
        "data": movie
    }


@movie_router.get("/movies/{movie_id}", response_model=schema.Movie)
def get_movie(movie_id: int,  db: Session = Depends(get_db)):
    '''Get a single movie'''
    movie = movies_service.get_single_movie(db, movie_id)
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    return movie
@movie_router.put("/movies/{movie_id}")
def update_movie(movie_id: int, movie: schema.MovieUpdate, user: schema.User = Depends(get_current_user), db: Session = Depends(get_db)):
    '''Update a movie'''
    updated_movie = movies_service.update_movie(db=db, movie_id=movie_id, movie=movie, user_id=user.id)
    if not updated_movie:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to update this movie")
    return updated_movie

@movie_router.delete("/movies/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_movie(movie_id: int, user: schema.User = Depends(get_current_user), db: Session = Depends(get_db)):
    
    '''Delete a movie'''
    movie = movies_service.delete_movie(db=db, movie_id=movie_id, user_id=user.id)
    if movie is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete this movie")
    logger.info("Movie deleted successfully with ID: %d", movie_id)
    return {
        "message": "Movie deleted successfully"
    }