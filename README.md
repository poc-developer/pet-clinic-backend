# pet-clinic-backend

This is a Flask-based REST API project that manages owners ad their pets. An owner can have multiple pets,
but each pet belongs to one owner. The API provides endpoints to create new owner, retrieve all owner details along with 
their pets or matching owners with the last name provided, and update existing owner's details.

## Table of Contents
- [Getting Started](#getting-started)
- [Setup Environments](#setup-environments)
- [Setup Database](#set-up-database)
- [API Endpoints](#api-enpoints)
- [Running Tests](#running-tests)
- [Running Application](#running-application)
- [Project Structure](#pro)
# Getting Started
**Prerequisites**
The following items should be installed in your system:
1. Python 3.12.0 or later
2. Github Desktop/ Git command line tool
3. VS Code
4. Postman
5. PostgreSQL 16.3 or later
6. pgAdmin (GUI tool)

# Setup Environments
1. **Clone the repository:**
```sh
    git clone https://github.com/poc-developer/pet-clinic-backend.git
```
2. **Redirect to the cloned repository:**
```sh
    cd pet-clinic-backend
```
3. **Create a virtual environment on VS Code:**
```sh
    python -m venv venv
```
4. **Activate the virtual environment:**
```sh
    venv/Scripts/activate
```
5. **Install the dependencies:**
```sh
    pip install -r requirements.txt
```

# Setup Database 
It is important to setup a relational database to store data. For this application, SQLite db has been used for testing and PostreSQL has been use for deployment. The `DATABASE_URL` environment variable has been store in `.env`.

### Using pgAdmin setup database:

1. **Download and install pgAdmin:**
- You can download pgAdmin from the [pgAdmin official website](https://www.pgadmin.org/download/)

2. **Create a new server in pgAdmin:**
- Open pgAdmin and right-click on "Servers" in the left navigation panel. 
- Click "Create" and then "Server".

3. **Configure the new server:**
- In the "General" tab, enter "localhost" as your server name.
- In the "Connection" tab, enter the following details:
    - Hostname/address: `localhost`
    - Port: `5432`
    - Maintenance database: `postgres`
    - Username: `your_postgresql_username`
    - Password: `your_postgresql_password`
- Click "Save"
4. **Create a new database**
- Expand the server you just created in the left navigation panel.
- Right-click on the "Database" and select "Create" -> ""Database..."
- Enter the name of the database (`PetClinicDB`) and click "Save"
5. **Create schemas for the database**
- Open the query tool and run the code in `sql/schema.sql`. This will create schemas for the database. 
6. **Insert sample data into tables**
- Run the code in `sql/owners.sql` and `sql/pets.sql` to insert sdample data for the tables.

### Accessing the Database in Python 
Once the database is set up, you need to ensure that the `DATABASE_URL` environment variable in `.env` is properly set. This ensure
it point to your PostgreSQL database. The model has been configured in `models.py`. 

# API Enpoints
### GET Owners
- **URL**: `/v1/owners`
- **Method**: `GET`
- **Descriptions**: Retrieves all owners.
- **Response**:
    ```json
    {
        "data":[
            {
                "id":1,
                "name": "John Doe",
                "address": "123 Main St",
                "city": "Somewhere",
                "telephone": "1111111111",
                "pets": [
                    {
                        "id": 1,
                        "name": "Kitty",
                        "birth_date": "01 May 2020",
                        "type": "cat"
                    },...
                ] 
            },...
        ]
    }
    ```

### GET Single Owner
- **URL**: `/v1/owners/<lastName>`
- **Method**: `GET`
- **Descriptions**: Retrieves owners with a matching last name.
- **Parameters**:
    - `lastName`: The last name to filter owners.
- **Response**:
    ```json
    {
        "data":[
            {
                "id":1,
                "name": "John Doe",
                "address": "123 Main St",
                "city": "Somewhere",
                "telephone": "1111111111",
                "pets": [
                    {
                        "id": 1,
                        "name": "Kitty",
                        "birth_date": "01 May 2020",
                        "type": "cat"
                    },...
                ] 
            },...
        ]
    }
    ```

### CREATE Owner
- **URL**: `/v1/owners/new`
- **Method**: `POST`
- **Descriptions**: Create a new owner.
- **Request Body**:
    ```json
    {
        "firstName": "John",
        "lastName": "Doe",
        "address": "123 Main St",
        "city": "Somewhere",
        "telephone": "1111111111"
    }
    ```
- **Response**:
    ```json
    {
        "data":{
                "id":1,
                "name": "John Doe",
                "address": "123 Main St",
                "city": "Somewhere",
                "telephone": "1111111111"
        },
        "message": "Owner Has Successfully Created!"
    }
    ```
### UPDATE Owner
- **URL**: `/v1/owners/<owner_id>/edit`
- **Method**: `PUT`
- **Descriptions**: Updates an owner's details.
- **Request Body**:
    ```json
    {
        "firstName": "John",
        "lastName": "Smith",
        "address": "123 Main St",
        "city": "Somewhere",
        "telephone": "1111111111"
    }
    ```
- **Response**:
    ```json
    {
        "data":{
                "id":1,
                "name": "John Smith",
                "address": "123 Main St",
                "city": "Somewhere",
                "telephone": "1111111111"
        },
        "message": "Owner Detail Updated Successfully!"
    }
    ```

# Running Tests
During testing, TestingConfig Class is specifically tailored for testing purpse. it overides the main application database URI to use an 
in-memory SQLite database 'sqlite:///:memory:' for tests. This is setup because an in-memory database is emphemeral and reset with each run,
suitable for fast, isolated test without the need for a persistent state. 
**Run the tests with pytest** 
```sh
    python -m pytest --cov=app tests/
```

# Running Application
To run the application, make sure you navigate to the correct directory.
1. **Run the command line in powershell**
```sh
    python run.py
```

2. **Access the API:**
The API will be available at `http://127.0.0.1:8081`. This API can be access using Postman. 

# Project Structure
```
|-.venv
|-app
|   |-configs
|       |-logging_config.py
|       |-model_config.py
|   |-models
|       |-model.py
|   |-routes
|       |-owners_routes.py
|       |-pets_routes.py
|   |-main.py
|-static
|   |-swagger.json
|-sql
|   |-DB_users.sql
|   |-owners.sql
|   |-pets.sql
|   |-schema.sql
|-tests
|   |-conftest.py
|   |-functional
|       |-test_routes.py
|   |-unit
|       |-test_models.py
|-.env
|-README.md
|-requirements.txt
|-run.py
```