# Use official lightweight Python 3.10 image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Create and configure virtual environment properly using ENV
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Upgrade pip inside virtual environment
RUN pip install --upgrade pip

# Copy and install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code into container
COPY . .

# Expose port for FastAPI backend
EXPOSE 8000

# Default command to launch the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]