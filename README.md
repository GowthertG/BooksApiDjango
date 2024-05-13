# BooksApiDjango


## Overview
BooksApiDjango is a Django REST framework application that provides an API for managing a collection of books. This repository serves as a starting point for building a backend system to manage books.

## Prerequisites
Before running the application, ensure you have the following installed:
- Python 3.x
- Django
- Django REST Framework

## Installation
1. Clone this repository to your local machine.
```bash
git clone https://github.com/GowthertG/BooksApiDjango.git
```
2. Navigate to the project directory.
```bash
cd BooksApiDjango
```
## Setting up Virtual Environment and Install requirements

1. Create a Virtual Environment:

    Navigate to your project directory and run the following command to create a virtual environment named `.venv`:
    
    ```bash
    python3 -m venv .venv
    ```

2. Activate the Virtual Environment:

    - **macOS/Linux:**
    
        ```bash
        source .venv/bin/activate
        ```

    - **Windows:**
    
        ```bash
        .venv\Scripts\activate
        ```

3. Install requirements:

    Run the following command to install requirements inside your virtual environment:
    
    ```bash
    pip install -r requirements.txt
    ```
## Running the Application
1. Apply migrations to create the database schema.
```bash
python manage.py migrate
```
2. Run the development server.
```bash
python manage.py runserver
```
3. Access the API at http://127.0.0.1:8000/.

## API Endpoints
- `/`: 
  - **Description:** Endpoint to list all books.
  
  More endpoints for CRUD operations are under development and will be added soon.

## Usage
- Access the application at `http://127.0.0.1:8000/` to view the list of all books.
