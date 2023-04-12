#!/bin/bash

python3 ./src/manage.py makemigrations
python3 ./src/manage.py migrate
sudo docker compose build
sudo docker compose up
