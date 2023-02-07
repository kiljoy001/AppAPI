$!/bin/sh

export FLASK_APP=./AppAPI/app.py
pipenv run flask --debug -h 0.0.0.0