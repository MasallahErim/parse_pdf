# Base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y apt-utils
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0 libsm6 libxext6 libxrender-dev libgomp1
RUN apt-get install -y poppler-utils

RUN apt-get install -y build-essential libpoppler-cpp-dev pkg-config python3-dev

# Tesseract'ı yükle
RUN apt-get install -y tesseract-ocr

# pikepdf'i yükle
RUN pip install pikepdf


# Copy the application code into the container
COPY . .

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port the app runs on
EXPOSE 8888

# Run the application
CMD ["python", "app.py"]
