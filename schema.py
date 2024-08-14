from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    email: str
    password: str

    model_config = ConfigDict(from_attributes=True)


class User(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class MovieBase(BaseModel):
    title: str
    description: str
    release_date: Optional[datetime] = None

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)

class MovieUpdate(MovieBase):
    pass

class RatingBase(BaseModel):
    rating: int

class RatingCreate(RatingBase):
    pass

class Rating(RatingBase):
    id: int
    movie_id: int
    user_id: int


    model_config = ConfigDict(from_attributes=True)

class CommentBase(BaseModel):
    content: str
    parent_comment_id: Optional[int] = None

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    user_id: int
    movie_id: int

    model_config = ConfigDict(from_attributes=True)

class CommentUpdate(CommentBase):
    pass
