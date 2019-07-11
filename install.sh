#!/usr/bin/env bash

echo
echo "INSTALLATION SCRIPT"
echo
echo "Enter a key to proceed..."
read key
echo

## 1) Install dependencies (Django)
echo
echo "Installing dependencies (django)..."
pip install --upgrade pip
pip install -r ./requirements.txt 
echo "done"

## 2) Create the database
echo
echo "Create the sqlite database..."
./manage.py makemigrations  
./manage.py migrate
echo "done"

## 3) Create an admin user
echo
echo "Creating an admin user (you)..."
./manage.py createsuperuser

## 4) Run the tests
echo
echo "Running the tests..."
./manage.py test myknowapp  
echo "done"

