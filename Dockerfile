FROM python:3.8

COPY . /app

WORKDIR /app

RUN pip install requirements.txt

cmd ["python", "app/main.py"]