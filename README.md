# FastAPI crud app

This repository showcases a basic CRUD (Create, Read, Update, Delete) application built using FastAPI designed for managing employee information. It provides a foundation for building more complex APIs and demonstrates core FastAPI functionalities.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Features

- **CRUD Operations:** Implements standard CRUD operations for managing employee data.
- **FastAPI Framework:** Utilizes FastAPI for building the API with automatic data validation and API documentation.
- **Data Models:** Defines data models using Pydantic for request and response bodies.
- **Example Endpoints:** Includes example endpoints for retrieving, creating, updating and deleting employee records.

## Installation

To set up the project locally, follow these steps:

1.  Clone the repository:

    ```bash
    git clone https://github.com/panoschron97/FastAPI_Crud_App
    cd FastAPI_Crud_App
    ```

2.  Create a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  Install the dependencies:

    ```bash
    pip install fastapi uvicorn pydantic
    ```

## Usage

1.  Run the FastAPI application using Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```

    This command starts the server, and you can access the API at `http://127.0.0.1:8000`. The `--reload` flag enables automatic reloading of the server on code changes.

2.  Interact with the API using tools like `curl`, Postman, or a web browser.  Example API endpoints:

    -   `GET /`: Returns a welcome message.
    -   `GET /api/employees`: Retrieves all employees.
    -   `GET /api/employees/{employeeid}`: Retrieves an employee by ID.
    -   `POST /api/employees`: Creates a new employee.  Requires a JSON payload matching the `information` model.
    -   `PUT /api/employees`: Updates an existing employee. Requires `employeeid` as a query parameter and a JSON payload.
    -   `DELETE /api/employees/{employeeid}`: Deletes an employee by ID.

## Dependencies

-   **FastAPI:** A modern, fast (high-performance) web framework for building APIs with Python.
-   **Uvicorn:** An ASGI (Asynchronous Server Gateway Interface) server for running FastAPI applications.
-   **Pydantic:** A data validation and settings management library.
