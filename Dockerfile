FROM python:3.11.3-slim

EXPOSE 8086

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN apt-get update
RUN apt-get -y --no-install-recommends install libpq-dev
RUN apt-get -y --no-install-recommends install python-dev
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# Creates a non-root user and adds permission to access the /app folder
RUN useradd appuser && chown -R appuser /app
USER appuser

ENTRYPOINT ["uvicorn","app.main:app","--port","8000","--host","0.0.0.0"]