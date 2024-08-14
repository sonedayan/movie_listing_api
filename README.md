# movie_listing_api
API that allows users to list movies, view listed movies, rate them, and add comments.

# Project Overview
The goal of this capstone project is to develop a movie listing API using FastAPI. The API will allow users to list movies, view listed movies, rate them, and add comments. The application will be secured using JWT (JSON Web Tokens), ensuring that only the user who listed a movie can edit it. The application should be hosted on a cloud platform.

## Requirements
* **Language & Framework:** Python using FastAPI
* **Authentication:** JWT for securing endpoints
* **Database:** Any SQL or NoSQL database
* **Testing:** Include unit tests for the API endpoints
* **Documentation:** API documentation using OpenAPI/Swagger
* **Logging:** Log important details of your application
* **Deployment:** Deploy your application on a cloud server of your choice.

## Features

### User Authentication:
User Registration
User login
JWT token generation

### Movie Listing:
* View a movie added (public access)
* Add a movie (authenticated access)
* View all movies (public access)
* Edit a movie (only by the user who listed it)
* Delete a movie (only by the user who listed it)

### Movie Rating:
* Rate a movie (authenticated access)
* Get ratings for a movie (public access)

### Comments:
* Add a comment to a movie (authenticated access)
* View comments for a movie (public access)
* Add comment to a comment i.e nested comments (authenticated access)

## Submission

Push your code to a public repository. Make sure your code is well documented with a requirement.txt file for your dependencies and a well-described README in your repository.

