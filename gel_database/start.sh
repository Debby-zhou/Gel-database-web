#!/bin/bash
pip install pymysql&&
python manage.py collectstatic --noinput&&
python manage.py makemigrations&&
python manage.py migrate&&
uwsgi --ini uwsgi.ini

