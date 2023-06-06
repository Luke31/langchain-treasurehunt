# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the poetry.lock and pyproject.toml files to the container
COPY pyproject.toml poetry.lock ./

# Install Poetry
RUN pip install --no-cache-dir poetry==1.4.2

# Install project dependencies using Poetry
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Copy the Flask application code to the container
# COPY app.py .  # mounted in volume for hot-reload

EXPOSE 5001
CMD ["poetry", "run", "python", "app.py"]
# CMD ["poetry", "run", "flask", "--app", "app.py", "--debug", "run", "-h", "0.0.0.0", "-p", "5001"]
