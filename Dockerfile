# Use Python 3.10
FROM python:3.10.14-slim

# Set working directory
WORKDIR /app

# Prevent interactive prompts
ENV PYTHONUNBUFFERED=1

# Copy & install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Default port (Render injects $PORT at runtime)
ENV PORT=8000

# Start uvicorn, use sh -c so ${PORT} is expanded
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT}"]
