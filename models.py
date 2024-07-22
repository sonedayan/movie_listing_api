from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, DateTime, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)

    movies = relationship('Movie', back_populates='user')
    ratings = relationship('Rating', back_populates='user')
    comments = relationship('Comment', back_populates='user')

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    release_date = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='movies')
    ratings = relationship('Rating', back_populates='movie')
    comments = relationship('Comment', back_populates='movie')

class Rating(Base):
    __tablename__ = 'ratings'
    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer, CheckConstraint('rating >= 1 AND rating <= 10'), nullable=False)
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    movie = relationship('Movie', back_populates='ratings')
    user = relationship('User', back_populates='ratings')

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    movie = relationship('Movie', back_populates='comments')
    user = relationship('User', back_populates='comments')
