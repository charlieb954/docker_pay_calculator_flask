FROM python:3.10-alpine

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5001

CMD ["gunicorn", "-b", "0.0.0.0:5001", "--chdir", "./app", "app:app", "--log-level=debug", "--workers=2"]