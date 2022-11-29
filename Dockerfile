FROM python:3.9-alpine3.13
LABEL mantainer="libcs.me"

ENV PYTHONBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN apk add --no-cache jpeg-dev zlib-dev
RUN pip install -r requirements.txt
RUN apk del .tmp
COPY . /app
EXPOSE 8000
