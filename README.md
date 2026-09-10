# Dockerized Flask API

**Student Name:** Pabarashmi Bandara
**Student ID:** 245011N
**Github Repository Link:** (https://github.com/PabarashmiBandara/docker_containerization_lab.git)

## Description

This project is a small Flask REST API containerized using Docker. It provides two endpoints: `/` and `/health`.

## Requirements

* Docker Desktop
* Docker Compose

No separate Python installation is required to run the application.

## Run the Application

From the project root directory, run:

```bash
docker compose up --build
```

The API will be available at:

```text
http://localhost:5000/
http://localhost:5000/health
```

### Endpoints

**GET /**

Returns the student information and a greeting message.

**GET /health**

Returns:

```json
{
  "status": "ok"
}
```

## Stop the Application

To stop and remove the containers, run:

```bash
docker compose down
```

## Limitations

This is a simple demonstration API and does not use a database or persistent storage. It is intended for local development and assignment demonstration rather than production use.

# Reflection

### 1. Image vs Container

The Docker image is the read-only template containing my Flask API, Python runtime, and dependencies. The container is the running instance created from that image. In my project, I built the image and then used it to run the API container.

### 2. Dockerfile Choice

I used `python:3.12-slim` as the base image because it provides the required Python environment while keeping the image lightweight. If I changed or removed this base image incorrectly, the required Python environment might not be available and the API would fail to run.

### 3. First Real Error

My first real error occurred because **Docker was not running**. When I tried to execute the Docker command, it could not connect to Docker. I opened Docker Desktop and waited until it was fully running. I then ran the command again successfully. This taught me that Docker Desktop must be running before Docker commands can be executed.