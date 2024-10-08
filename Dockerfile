# Use a base image with Python and Streamlit pre-installed.  This reduces image size.
FROM python:3.9-slim-bullseye

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

EXPOSE 8501
# Run the web server on container startup
ENTRYPOINT ["streamlit", "run", "app.py","--server.port=8501","--server.address=0.0.0.0"]
