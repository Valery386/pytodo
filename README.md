# PyToDo

PyToDo is a Django-based To-Do app designed to help you manage your daily tasks efficiently. It provides a simple and
user-friendly interface to create, update, delete, and view tasks.

## Features

- **Task Management**: Create, update, and delete to-dos.
- **Django Framework**: Built using the Django web framework for fast and scalable development.
- **Flexible and Extensible**: Designed to allow easy extensions and customizations.

## Installation

### Prerequisites

- Python >= 3.13.3
- Pipenv (for managing the Python environment)
- Django

### Steps

1. Clone the repository:
    ```bash
    git clone <REPO_URL>
    cd pytodo
    ```

2. Set up the virtual environment and install dependencies:
    ```bash
    pipenv install
    pipenv shell
    ```

3. Run database migrations:
    ```bash
    python manage.py migrate
    ```

4. Start the development server:
    ```bash
    python manage.py runserver
    ```

5. Visit `http://127.0.0.1:8000/` in your web browser to use the app.

## Configuration

Create a `.env` file in the project root for environment variables. Example:

```
# Django settings
env DEBUG=True 
SECRET_KEY=<your-secret-key> 
ALLOWED_HOSTS=localhost,127.0.0.1

# Database settings
DB_ENGINE=django.db.backends.postgresql
DB_NAME=<DB-name>
DB_USER=<your-user>
DB_PASSWORD=<your-password>
DB_HOST=localhost
DB_PORT=5432
```

## App Structure

The project contains the following components:

- `todo` app: The main app handling task-related functionality.
- `models.py`: Contains the `ToDo` model, which defines the structure of a to-do item.
- `views.py`: Handles the logic for creating, updating, and listing to-dos.
- `templates/`: Contains the HTML templates for the app.

## To-Do Model

The `ToDo` model (`todo.models.ToDo`) includes:

- `title`: The title of the task (string).
- `description`: Detailed description of the task (string).
- `created_at`: Timestamp when the task is created.
- `completed`: Boolean to indicate task completion.

## Usage

1. Add tasks through the interface and track their statuses.
2. Update or mark tasks as completed.
3. Delete tasks that are no longer needed.
