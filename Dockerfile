FROM python:3.11-alpine

# Keeps Python from generating .pyc files in the container, Turns off buffering for easier container logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Настрока времени
ENV TZ='UTC'
WORKDIR /app

RUN apk add --no-cache --virtual .build-deps gcc libc-dev make && \
    pip install --upgrade pip && \
    pip install poetry && \
    apk del .build-deps

COPY pyproject.toml pyproject.toml


RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi --with=dev

RUN rm /app/pyproject.toml

ADD src/. .
