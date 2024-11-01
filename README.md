# installation
install Python, version 3.12.6
install PostgreSQL 16.4 with PgBouncer and PgAgent
navigate to the project folder
create VM: python -m venv env
activate VM: .\env\Scripts\activate
deactive VM: deactivate
install requirements: pip install -r requirements.txt

# run and test
run the application: uvicorn app.main:app --reload
test a route with the swagger from fastAPI: http://127.0.0.1:8000/docs
example on how to use a curl to test a route:
    - for CMD:  curl -X GET "http://127.0.0.1:8000/items/0"
    - for powershell: curl.exe -X GET "http://127.0.0.1:8000/items/0"

# database
access the PostgreSQL shell: psql postgres
create a new database: CREATE DATABASE mydatabase;
create a new user: CREATE USER myuser WITH PASSWORD 'mypassword';
grant privileges: GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;

