FROM python:3.10.7-alpine

ENV PYTHONBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY ./ /app
RUN pip install psycopg2-binary 
RUN pip install -r requirements.txt