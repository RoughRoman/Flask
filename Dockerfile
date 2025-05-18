FROM python:3.11-slim

WORKDIR /api-flask

# Copy the application files into the container
COPY . /api-flask/

# Install dependencies from the requirements file
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Expose port 80 for the Flask app
EXPOSE 80

# Run the Flask app
CMD ["python", "main.py"]
