from fastapi import APIRouter, status

movie_router = APIRouter(
    prefix= "/movies",
    tags= ["movies"]
)

@movie_router.get("/", status_code=status.HTTP_200_OK)
def get_movies():
    pass

@movie_router.post("/", status_code=status.HTTP_202_ACCEPTED)
def create_movie():
    pass

@movie_router.get("/{movie_id}")
def get_movie(movie_id: int):
    pass

@movie_router.put("/{movie_id}")
def update_movie(movie_id: int):
    pass
