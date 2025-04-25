# Use the official Python image as the base
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory to the container's working directory
COPY . .

# Install required Python packages listed in requirements.txt
RUN pip install -r requirements.txt

# Expose port 5000 to the host (Flask default port)
EXPOSE 5000

# Run the Flask app (assumes the main file is app.py)
CMD ["python", "app.py"]


