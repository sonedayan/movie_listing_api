from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    username: Optional[str] = None
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class MovieBase(BaseModel):
    title: str
    description: Optional[str] = None
    release_date: Optional[datetime] = None

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)

class RatingBase(BaseModel):
    rating: int
    movie_id: int
    user_id: int

class RatingCreate(RatingBase):
    pass

class Rating(RatingBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class CommentBase(BaseModel):
    content: str
    movie_id: int
    user_id: int

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
