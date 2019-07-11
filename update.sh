#!/usr/bin/env bash

echo
echo "UPDATE SCRIPT"
echo
echo "Enter a key to proceed..."
read key
echo


## 1) Update source code
echo
echo "Updating source code (git pull)..."
git pull
echo "done"

## 2) Update the database
echo
echo "Updating the database (migrations)..."
./manage.py makemigrations  
./manage.py migrate
echo "done"

## 3) Run the tests
echo
echo "Running the tests..."
./manage.py test myknowapp  
echo "done"
