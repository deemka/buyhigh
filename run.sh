#!/usr/bin/env bash

# Service up, pgdata not ready?
until ./manage.py migrate
do
    sleep 2
done

./manage.py createsuperuser --noinput 2>/dev/null
./manage.py runserver 0:8000
