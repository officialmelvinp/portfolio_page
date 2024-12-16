#!/bin/bash
# Install Python if it's not available
if ! command -v python3 &> /dev/null; then
    echo "Python is not installed. Installing Python..."
    apt-get update && apt-get install -y python3 python3-pip
fi

# Upgrade pip
python3 -m pip install --upgrade pip

# Install requirements
python3 -m pip install -r requirements.txt

# Run collectstatic
python3 manage.py collectstatic --noinput