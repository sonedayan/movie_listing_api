from fastapi import FastAPI
from routers.authentication import auth_router
from routers.movies import movie_router
from routers.comments import comment_router
from routers.ratings import rating_router
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title= "Movie Listing API",
    description="An API for managing a list of movies",
)

app.include_router(router = auth_router)
app.include_router(router = movie_router)
app.include_router(router = rating_router)
app.include_router(router = comment_router)

