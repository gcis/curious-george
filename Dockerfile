FROM python:2.7

COPY app /app

WORKDIR /app

pip install boto3

CMD [ "python", "main.py" ]