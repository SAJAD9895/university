#!/bin/bash

# Upgrade pip and install requirements
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Run collectstatic
python3 manage.py collectstatic --noinput