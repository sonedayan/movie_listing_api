from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import schema
from services import ratings_service
from database import get_db

rating_router = APIRouter(
    prefix="/ratings",
    tags=["Ratings"]
)

@rating_router.post("/", response_model=schema.Rating)
def create_rating(rating: schema.RatingCreate, db: Session = Depends(get_db)):
    return ratings_service.create_rating(db=db, rating=rating)

@rating_router.get("/{movie_id}", response_model=List[schema.Rating])
def read_ratings(movie_id: int, db: Session = Depends(get_db)):
    ratings = ratings_service.get_ratings(db, movie_id=movie_id)
    return ratings
