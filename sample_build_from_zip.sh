#!/bin/bash

cd TameofThrones-master
pip install flake8 pytest pytest-cov
python -m unittest -v tameofthrones.test_tameofthrones
flake8 --exclude=venv* --statistics
pytest -v --cov=tameofthrones
python tameofthrones/tameofthrones.py
