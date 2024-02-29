# noted. (Backend Server in Python)

## Overview
This project involves the conversion of a backend server originally written in JavaScript with Node.js and Express into Python using FastAPI, Pydantic, and Pymongo. The primary goal of this project is to learn Python while gaining hands-on experience with modern Python web development frameworks and tools.


## Technologies Used
- FastAPI version: 0.110.0
- Pydantic version: 2.6.2
- Pymongo version: 4.6.2
- Python-dotenv version: 1.0.1

## Installation
1. Clone the repository: `git clone https://github.com/yurikahirata/noted_backend_python.git`
2. Navigate to the project directory: `cd noted_backend_python`
3. Install dependencies: `pip install -r requirements.txt`

## Usage
1. You will need to create a .env file in the backend-python folder with variables ATLAS_URI and DB_NAME
```
ATLAS_URI=<Please contact the administrator for this URI>
DB_NAME=noted
```
3. Start the FastAPI server: `cd backend-python` and `python -m uvicorn main:app --reload`
4. Access the API endpoints using a web browser or API client like Postman.
