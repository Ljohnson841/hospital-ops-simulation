# Install base Python image
FROM python:3.11-slim
    # Set the Working Directoty
    WORKDIR /app
    # Copy the dependencies file
    COPY requirements.txt ./
    # Install the dependencies
    RUN pip install --no-cache-dir -r requirements.txt
    # Copy the app files
    COPY . .
    # Run the app
    CMD ["python", "src/ingest.py"]
