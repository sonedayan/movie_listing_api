from sqlalchemy.orm import Session
import models, schema


def get_ratings_per_movie(db: Session, movie_id: int):
    return db.query(models.Rating).filter(models.Rating.movie_id == movie_id).all()

def get_rating(db: Session, rating_id: int):
    return db.query(models.Rating).filter(models.Rating.id == rating_id).first()

def update_rating(db: Session, rating_id: int, new_rating: schema.RatingCreate, user_id: int):
    db_rating = db.query(models.Rating).filter(models.Rating.id == rating_id, models.Rating.user_id == user_id).first()
    if db_rating:
        db_rating.rating = new_rating.rating
        db.commit()
        db.refresh(db_rating)
    return db_rating

def create_rating(db: Session, rating: schema.RatingCreate, user_id: int, movie_id: int):
    db_rating = models.Rating(
        rating=rating.rating,
        user_id=user_id,
        movie_id=movie_id
    )
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating
    # if db_rating:
    #     db_rating = models.Rating(**rating.model_dump(), user_id=user_id, movie_id=movie_id)
    #     db.add(db_rating)
    #     db.commit()
    #     db.refresh(db_rating)
    # return db_rating


def delete_rating(db: Session, rating_id: int, user_id: int):
    db_rating = db.query(models.Rating).filter(models.Rating.id == rating_id, models.Rating.user_id == user_id).first()
    if db_rating:
        db.delete(db_rating)
        db.commit()
    return db_rating is not None