#!/bin/bash

# Ensure pip is installed (if not already present)
if ! python -m pip --version; then
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
fi

# Upgrade pip to the latest version
python -m pip install --upgrade pip

# Install dependencies from requirements.txt
python -m pip install -r requirements.txt

# Run collectstatic (no input required)
python manage.py collectstatic --noinput
