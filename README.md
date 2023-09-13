This README provides the project description and instructions on how to set up, run and use the Application Programming Interface (API) that was created as a result of this project.

## Table of Contents
- [Description of the project](#description-of-the-project)
- [Link to UML class diagram](#link-to-uml-class-diagram)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
    - [Running the API](#running-the-api)
    - [Endpoints](#endpoints)
- [Contributing](#contributing)
- [Author](#author)

## Description of the project
The goal of the project is to build a simple REST API, interfacing with database of choice, in this case an sqlite database, capable of Create, Read, Update, and Delete (CRUD) operations on a "person" operations.

## Link to UML class diagram
https://docs.google.com/drawings/d/1-nPxFs_I5geLtUKT917wlgDJXEPnc4rq2BNvXwAf6BY/edit?usp=drivesdk

## Prerequisites
Before you begin, ensure you have the following prerequisites installed in your system:
- Python (3.8 or higher)
- pip (Python package manager)
- pipenv
- git bash terminal (For windows)

## Installation
1. Clone this repository:
git clone
https://github.com/Chiemelie10/hng_task_two_crud

2. Create a virtual environment:
Run the command "pipenv shell" while in the directory you just cloned.

## Usage
To run the API, execute the following command from the project root directory:
python app.py
The API will be accessible at 'http://localhost:5000'.

### Endpoints
The API provides the following endpoints:
- **GET /api; Retrieves a list of all users.
- **GET /api/<user_id:string>; Retrieve user details by ID.
- **POST /api; Create a new user.
- **PUT /api/<user_id:string>; Update user details by ID.
- **PATCH /api/<user_id:string>; Partially update user details by ID.
- **DELETE /api/<user_id:string>; Delete a user by ID.

You can access these endpoints using a tool like 'curl', 'Postman', or any HTTP client.

Examples:

- Retrieve all users:
GET http://localhost:5000/api

- Create a new user:
POST http://localhost:5000/api
{
    "name": "Eze Chiemelie"
}

- Update a user by ID:
PUT http://localhost:5000/api/<user_id:string>
{
    "name": "Updated Name"
}

## Contributing
Contributions are welcome! Please fork this repository an submit a pull request with your improvements.

## Author
Eze Taslim Chiemelie (chiemelieeze@gmail.com)