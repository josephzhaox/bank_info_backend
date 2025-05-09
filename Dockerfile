# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables (optional, overridden in Cloud Run)
ENV FLASK_ENV=production
ENV PORT=8080
ENV PYTHONUNBUFFERED=1

# Run with gunicorn
# CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]
# Run the app with Gunicorn for production
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
