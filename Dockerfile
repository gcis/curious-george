FROM python:2.7

COPY app /app

WORKDIR /app

RUN pip install boto3

CMD [ "python", "-u", "main.py" ]