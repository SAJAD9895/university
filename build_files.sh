#!/bin/bash

# Upgrade pip and install requirements
python3.9 -m pip install --upgrade pip
python3.9 -m pip install -r requirements.txt

# Run collectstatic
python3.9 manage.py collectstatic --noinput