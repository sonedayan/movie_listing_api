
# AltSchool of Backend Engineering (Python) Tinyuka 2023 Capstone Project 

## Project Overview
The goal of this capstone project is to develop a movie listing API using FastAPI. The API will allow users to list movies, view listed movies, rate them, and add comments. The application will be secured using JWT (JSON Web Tokens), ensuring that only the user who listed a movie can edit it. The application should be hosted to a cloud platform.
## Requirements
1. Language & Framework: Python using FastAPI
2. Authentication: JWT for securing endpoints
3. Database: Any SQL or NoSQL database
4. Testing: Include unit tests for the API endpoints
5. Documentation: API documentation using OpenAPI/Swagger
6. Logging: Log important details of your application
7. Deployment: Deploy your application on a cloud server of your choice.
## Features
1. **User Authentication**:
    - User registration
    - User login
    - JWT token generation
2. **Movie Listing**:
    - View a movie added (public access)
    - Add a movie (authenticated access)
    - View all movies (public access)
    - Edit a movie (only by the user who listed it)
    - Delete a movie (only by the user who listed it)
3. **Movie Rating**:
    - Rate a movie (authenticated access)
    - Get ratings for a movie (public access)
4. **Comments**:
    - Add a comment to a movie (authenticated access)
    - View comments for a movie (public access)
    - Add comment to a comment i.e nested comments (authenticated access)
