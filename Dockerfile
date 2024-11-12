#Use the official Python image from the Docker Hub
FROM python:3.10-slim


#Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#Set the working directory
WORKDIR /app

#Copy the requirements file and install dependencies
RUN pip install Django

#Copy the rest of the project files
COPY . .

#Collect static files (optional step, useful in production)
RUN python manage.py migrate

#Expose port 8000 to access Django’s dev server
EXPOSE 8000

#Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]