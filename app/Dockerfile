FROM python:3.8.7-slim

COPY ./requirements.txt /
COPY ./entrypoint.sh /

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

WORKDIR /app

ENTRYPOINT ["sh", "/entrypoint.sh"]