## Step1: Project setup

    poetry new library
    - add flask and sqlalchemy into [tool.poetry.dependencies] of puproject.toml
    poetry shell
    poetry install  --> Installs the dependencies specified in pyproject.toml.
    pip list
    poetry export --without-hashes -f requirements.txt > requirements.txt

## Step1: Setup tables and initial data

    python database_setup.py 
    
## Step3: Run some tests on tables
    python3 tests/test_library.py

## Step4: Run the app from virtual environment

    flask run
    (or python3 main.py)