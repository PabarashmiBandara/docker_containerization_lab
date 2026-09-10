# Reflection

## 1. Image vs Container

The Docker image is the read-only template created from the Dockerfile, while the container is a running instance of that image. In my project, the image contains the Python runtime, Flask dependency and API source code. The container runs this packaged application and provides the isolated environment for the API.

## 2. Dockerfile Choice

I copied requirements.txt and installed the dependencies before copying the application source. This improves Docker build caching because the dependency installation layer can be reused when only the source code changes. If I copied the entire project before installing the dependencies, changes to source files could invalidate the dependency layer and make rebuilds slower.

## 3. First Real Error

My first error occurred because Docker Desktop was not running.

Cannot connect to the Docker daemon.
Is the docker daemon running?

I started Docker Desktop and waited until it was running. After that, I ran the Docker command again successfully. This showed me that Docker Desktop must be running before using Docker commands.