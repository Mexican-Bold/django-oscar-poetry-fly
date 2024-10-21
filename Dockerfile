ARG PYTHON_VERSION=3.11-slim

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

RUN pip install poetry
COPY pyproject.toml poetry.lock /code/
RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-root --no-interaction
COPY . /code

ENV SECRET_KEY "B147SFHzNrSYB4C7fLQckD6UUJY0Pkz9LMzc7EdhIJ484GhdHm"
RUN python manage.py collectstatic --noinput
RUN chmod +x startup.sh
EXPOSE 8000
ENTRYPOINT ["./startup.sh"]

#CMD ["gunicorn","--bind",":8000","--workers","2","djospofly_01.wsgi"]

RUN apt-get update && apt-get install -y \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

