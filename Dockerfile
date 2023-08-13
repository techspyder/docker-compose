#Use official python image as base image
FROM python:3.8

#Set working dir inside container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

#Install packages specified in requirements.txt
RUN pip install -r requirements.txt

#Copy rest of the application into container
COPY . .
# Expose port 5000
EXPOSE 5000
# Specify the command to run when the container starts
CMD ["python", "app.py"]

