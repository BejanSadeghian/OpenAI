FROM python:3

# Install python packages for function
RUN pip install jupyter sqlalchemy psycopg2

# Install python packages for development
RUN pip install pre-commit pylint black mypy bandit


RUN apt update
RUN apt -y install postgresql postgresql-contrib

COPY .pre-commit-config.yaml .
RUN git init . && pre-commit install-hooks
