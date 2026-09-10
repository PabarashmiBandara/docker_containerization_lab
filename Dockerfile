# Use a sensible, lightweight base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy only the requirements first to leverage Docker caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Document the port
EXPOSE 5000

# Start the application using the exec form
CMD ["python", "app.py"]