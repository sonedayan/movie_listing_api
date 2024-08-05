from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services import movies_service
import schema as schema
from authentication import get_current_user

movie_router = APIRouter(
    prefix= "/movies",
    tags= ["Movies"]
)

@movie_router.get("/", status_code=status.HTTP_200_OK)
def get_movies(db: Session = Depends(get_db), user: schema.User = Depends(get_current_user), offset: int = 0, limit: int = 10):
    movies = movies_service.get_movies(db, user_id=user.id, offset=offset, limit=limit)
    return {
        "message": "Movies retrieved successfully",
        "data": movies
    }

@movie_router.post("/", status_code=status.HTTP_202_ACCEPTED)
def create_movie(payload: schema.MovieCreate, user: schema.User = Depends(get_current_user), db: Session = Depends(get_db)):
    movie = movies_service.create_movie(db=db, movie=payload, user_id=user.id)
    return {
        "message": "Movie created successfully",
        "data": movie
    }


@movie_router.get("/{movie_id}")
def get_movie(movie_id: str, user: schema.User = Depends(get_current_user), db: Session = Depends(get_db)):
    '''Get a single movie'''
    movie = movies_service.get_single_movie(db=db, movie_id=movie_id ,user=user)
    if movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {
        "message": "Movie retrieved successfully",
        "data": movie
    }

@movie_router.put("/{movie_id}")
def update_movie(movie_id: int, payload: schema.MovieUpdate, db: Session = Depends(get_db)):
    '''Update a movie'''
    movie = movies_service.update_movie(db=db, movie_id=movie_id, payload=payload)
    if movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {
        "message": "Movie updated successfully",
        "data": movie
    }
