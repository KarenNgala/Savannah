FROM python:3.11-slim

ARG ENVIRONMENT
ENV ENVIRONMENT=${ENVIRONMENT}

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

RUN if [ "$ENVIRONMENT" = "prod" ]; then python manage.py collectstatic --noinput; fi

EXPOSE 8000

CMD if [ "$ENVIRONMENT" = "prod" ]; then gunicorn --bind 0.0.0.0:8000 savannah.wsgi:application; else python manage.py runserver 0.0.0.0:8000; fi