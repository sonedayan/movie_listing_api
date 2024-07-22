from sqlalchemy.orm import Session
import models, schema


def get_ratings(db: Session, movie_id: int):
    return db.query(models.Rating).filter(models.Rating.movie_id == movie_id).all()

def create_rating(db: Session, rating: schema.RatingCreate):
    db_rating = models.Rating(**rating.dict())
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating