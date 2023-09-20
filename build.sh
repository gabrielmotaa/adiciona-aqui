#!/bin/sh
set -o errexit

./manage.py collectstatic --no-input
./manage.py migrate
./manage.py shell -c "from django.contrib.auth import get_user_model;get_user_model().objects.filter(is_superuser=True).delete()"
./manage.py createsuperuser --noinput
./manage.py populate_categories