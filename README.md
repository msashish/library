## Step1: Project setup

    poetry new library
    - add flask and sqlalchemy into [tool.poetry.dependencies] of puproject.toml
    poetry shell
    poetry install  --> Installs the dependencies specified in pyproject.toml.
    pip list
    poetry export --without-hashes -f requirements.txt > requirements.txt

## Step1: Lets write library app now

    python database_setup.py 
    
