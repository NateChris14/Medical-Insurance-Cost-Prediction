#Creating a base image
FROM python:3.9

#Setting the working directory
WORKDIR /app

#Copying the application code
COPY . /app

#Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Exposing port
ENV PORT=8080
EXPOSE 8080

#Running the application:
CMD ["gunicorn","medapp:app"]
