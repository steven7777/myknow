

I - INSTALL

1) Create a venv and activate it

$ python3 -m venv venv_myknow

$ source ./venv_myknow/bin/activate

2) Install dependencies (Django)

(venv_myknow) $ pip install -r requirements.txt 

3) Create the database

(venv_myknow) $ ./manage.py makemigrations

(venv_myknow) $ ./manage.py migrate

4) Create an admin user

(venv_myknow) $ ./manage.py createsuperuser



II - RUN

(venv_myknow should be activated, see above)

1) Start web server

(venv_myknow) $ ./manage.py runserver

2) Go to myknow website

Connect to http://localhost:8000

From this webpage, there is a link "=> GO TO ADMIN SITE" to go to the ADMIN site in order to enter some entities into the database.
You can also go directly there:
Connect to http://localhost:8000/admin
Login as the admin user (created at step I-4 above)

