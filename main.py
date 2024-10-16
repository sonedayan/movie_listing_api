from fastapi import FastAPI
from routers.authentication import auth_router
from routers.movies import movie_router
from routers.comments import comment_router
from routers.ratings import rating_router
from database import engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title= "Movie Listing API",
    description="This project is a Movie Listing API built with FastAPI. The API allows authenticated users to list movies, view listed movies, rate them, and add comments. The application is secured using JWT (JSON Web Tokens), ensuring that only the user who listed a movie can edit or delete it.",
)

app.include_router(router = auth_router,  tags=["Authentication"])
app.include_router(router = movie_router, prefix="/api", tags=["Movies"])
app.include_router(router = rating_router, prefix="/api", tags=["Ratings"])
app.include_router(router = comment_router, prefix="/api", tags=["Comments"])

@app.get('/')
def home():
    return f"Welcome to Movie Listing API...navigate to /docs to view documentation"
