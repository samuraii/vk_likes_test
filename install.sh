#!/bin/bash

FILE=env/
ENV_FILE=.env

if [ ! -f "$ENV_FILE" ]; then 
    touch .env
    echo $'ACCESS_TOKEN=\nUSER_ID=\nVK_USER_ID=' > .env
fi

if [ -d "$FILE" ]; then
    source env/bin/activate &&
    pip install -U pip &&
    pip install -Ur requirements.txt
else
    python3 -m venv env &&
    source env/bin/activate &&
    pip install -U pip &&
    pip install -Ur requirements.txt
fi