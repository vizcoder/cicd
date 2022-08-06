FROM python:3.6

WORKDIR /app

COPY requirments.txt .

RUN pip install -r requirments.txt

COPY src /app


