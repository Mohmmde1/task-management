# Task Management System

This is a simple Task Management System implemented using Django and Django REST Framework. It allows users to manage tasks by providing (Create, Retrieve, Delete) functionalities via RESTful APIs.

## Features

- Create a new task with title, description, and completion status.
- Retrieve a list of tasks.
- Retrieve a task by ID
- Delete tasks by their ID.

## Technologies Used

- Python 3.12
- Django 5.0
- Django REST Framework 3.15
- SQLite (default database)

## API Endpoints

### Tasks

- **Create a Task**
  - URL: `POST /api/tasks/`
  - Description: Create a new task with title, description, and completion status.
  - Request Body:
    ```json
    {
      "title": "Task Title",
      "description": "Task Description",
      "completed": false
    }
    ```
  - Response: Returns the created task object.

- **List Tasks**
  - URL: `GET /api/tasks/`
  - Description: Retrieve a list of all tasks.
  - Response: Returns a list of task objects.

- **Retrieve a Task by ID**
  - URL: `GET /api/tasks/{task_id}/`
  - Description: Retrieve details of a specific task identified by `{task_id}`.
  - Response: Returns the task object with the specified ID.

- **Delete a Task**
  - URL: `DELETE /api/tasks/{task_id}/`
  - Description: Delete a task identified by `{task_id}`.
  - Response: Returns a success message upon successful deletion.


### Swagger API Documentation
 - **Explore and interact with the API using Swagger documentation:**
 - Swagger UI: http://127.0.0.1:8000/swagger/
 - Redoc: http://127.0.0.1:8000/redoc/

