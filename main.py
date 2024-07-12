from fastapi import FastAPI

app = FastAPI(
    title= "Movie Listing API",
    description="An API for managing a list of movies",
)

@app.get('/')
def home():
    return "Movie Listing Application"
