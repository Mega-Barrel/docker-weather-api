# Specify Docker Image
FROM alpine:latest

# Set environment variable
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

# Update package repositories and install python
# ensure that pip is available by running python3 -m ensurepip,
# Then, we upgrade pip and setuptools to the latest versions using pip3 install --upgrade pip setuptools
# Finally, we clean up the pip cache to reduce the image size.

RUN apk update && \
    apk add --no-cache python3 py3-pip

# SET WORKING DIR
WORKDIR /app

# Copy files from app to WORKDIR
COPY /app/main.py /app/main.py
COPY /requirements.txt /app/requirements.txt

# Install packages
RUN pip3 install --no-cache-dir -r requirements.txt

# SET ENVIRONMENT VARIABLE
ENV weather-api 'API Key'

# RUN the application
CMD [ "python3", "main.py"]