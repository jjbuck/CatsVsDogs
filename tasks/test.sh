#!/usr/bin/env bash

# Make sure you have activate the venv
# source venv/bin/activate
python3 -m pytest ./tests --cov-report term --cov=cats_vs_dogs -s