FROM python:3

RUN pip install --upgrade pip

# Setup a virtual env and activate it
RUN pip install virtualenv && \
    virtualenv .venv && \
    source ./venv/bin/activate

# Install python packages for function
RUN pip install ipykernel jupyter sqlalchemy psycopg2 poetry

# Install python packages for development
RUN pip install pre-commit pylint black mypy bandit


RUN apt update
RUN apt -y install postgresql postgresql-contrib

COPY .pre-commit-config.yaml .
RUN git init . && pre-commit install-hooks
