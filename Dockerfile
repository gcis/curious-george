FROM python:alpine

COPY app /app

WORKDIR /app

CMD [ "python", "main.py" ]