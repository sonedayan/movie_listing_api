from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import schema
from services import ratings_service, movies_service
from database import get_db
from authentication import get_current_user

rating_router = APIRouter(
    tags=["Ratings"]
)


## Creating a rating for a specific movie(Authenticated users only)
@rating_router.post("/movies/{movie_id}/ratings", response_model=schema.Rating, status_code=status.HTTP_201_CREATED)
def create_rating(movie_id: int, rating: schema.RatingCreate, user: schema.User = Depends(get_current_user), db: Session = Depends(get_db)):
    '''Create a rating for a movie'''
    # Check if movie exists
    movie = movies_service.get_single_movie(db, movie_id)
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    
    # Create and return the rating
    return ratings_service.create_rating(db=db, rating=rating, user_id=user.id, movie_id=movie_id)

## Retrieving all ratings for a specific movie
@rating_router.get("/movies/{movie_id}/ratings", response_model=List[schema.Rating])
def read_ratings(movie_id: int, db: Session = Depends(get_db)):
    # Check if movie exists
    movie = movies_service.get_single_movie(db, movie_id)
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    
    # Return all ratings for the movie
    return ratings_service.get_ratings_per_movie(db, movie_id)


## Retrieving a single rating by its id
@rating_router.get("/ratings/{rating_id}", response_model=schema.Rating)
def get_rating(rating_id: int, db: Session = Depends(get_db)):
    rating = ratings_service.get_rating(db=db, rating_id=rating_id)
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    return rating


## Updating a rating by its id(Allows an authenticated user to update their own rating)
@rating_router.put("/ratings/{rating_id}", response_model=schema.Rating)
def update_rating(rating_id: int, new_rating: schema.RatingCreate, db: Session = Depends(get_db), user: schema.User = Depends(get_current_user)):
    rating = ratings_service.get_rating(db=db, rating_id=rating_id)
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")

    if rating.user_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this rating")

    return ratings_service.update_rating(db=db, rating_id=rating_id, new_rating=new_rating, user_id=user.id)


## Allows authenticated users to delete their rating
@rating_router.delete("/ratings/{rating_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_rating(rating_id: int, db: Session = Depends(get_db), user: schema.User = Depends(get_current_user)):
    rating = ratings_service.get_rating(db=db, rating_id=rating_id)
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")

    if rating.user_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this rating")

    success = ratings_service.delete_rating(db=db, rating_id=rating_id, user_id=user.id)
    if not success:
        raise HTTPException(status_code=400, detail="Failed to delete rating")

    return {"detail": "Rating deleted successfully"}
