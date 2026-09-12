bash#!/usr/bin/env bash

set -o errexit
pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

#idk what this does

#TRANSFER DATA
#python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.permission --indent 4 -o datadump.json

#Run development server
#python -m uvicorn sunbeam.asgi:application --host 0.0.0.0 --port 8000 