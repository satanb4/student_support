# This is the Dockerfile for the build image. It is used to build the application.

FROM node:16-slim AS frontend

WORKDIR ./tailwindcss

COPY ./tailwindcss /tailwindcss
COPY ./app /app

RUN npm install
RUN npx tailwindcss -i /app/src/css/inputs.css -o build.css --minify

FROM python:3.11-slim-buster AS build

WORKDIR /usr/www/mypath

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY ./app ./app
COPY ./.env ./.env

COPY ./requirements/requirements.txt ./app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r ./app/requirements.txt

COPY --from=frontend /tailwindcss/build.css ./app/src/css/build.css
