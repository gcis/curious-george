FROM python:2.7

COPY app /app

WORKDIR /app

CMD [ "python", "main.py" ]