FROM python:latest

COPY app /app

WORKDIR /app

CMD [ "python", "main.py" ]