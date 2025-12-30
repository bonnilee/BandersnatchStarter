# Use official Python 3.13 slim image
FROM python:3.13-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    libssl-dev \
    && curl https://sh.rustup.rs -sSf | sh -s -- -y \
    && . $HOME/.cargo/env \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Add Rust to PATH
ENV PATH="/root/.cargo/bin:$PATH"
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose Flask port
EXPOSE 8000

# Environment variables
ENV FLASK_APP=app.main:APP
ENV FLASK_ENV=production

# Start the Flask app
CMD ["gunicorn", "app.main:APP", "-b", "0.0.0.0:8000", "--workers", "1"]


