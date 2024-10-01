FROM python:3

RUN apt-get update -y && \ 
  apt-get install -y

WORKDIR /app

RUN pip install Flask requests flask_mysqldb

COPY . .

EXPOSE 5000

CMD ["python", "./app.py"]