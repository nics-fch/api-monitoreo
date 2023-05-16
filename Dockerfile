FROM python:3.10.6-slim-buster

WORKDIR /app

COPY ./requirements.txt /code/requirements.txt

RUN apt-get update

RUN apt-get -y install libpq-dev

RUN apt-get -y install python-dev

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 8086

COPY ./app /code/app