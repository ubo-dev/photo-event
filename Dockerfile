# Dockerfile
# Use official Python image
FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy only pyproject.toml and poetry.lock first (for caching dependencies)
COPY pyproject.toml poetry.lock /app/

# Install dependencies
RUN poetry config virtualenvs.in-project true \
 && poetry install --no-root --no-interaction --no-ansi

# Copy the rest of the project
COPY . /app/

# Expose the port FastAPI runs on
EXPOSE 8000

# Run the app
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]