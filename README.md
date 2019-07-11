
# INTRO

MyKnow is a personal knowledge management web application,
allowing you to enter and describe any "entity" you know about and its relationships with other entities.
Then, you can compare these entities with each other, myknow being able to compare any entities which have common attributes.

It is based on the python framework Django v2.

This is a first very alpha version, work in progress.

Version : 0.1 (project started July 2019)

Author : Etienne Pallier 

---

# INSTALL

## 1) Create a venv and activate it

$ python3 -m venv venv_myknow  
$ source ./venv_myknow/bin/activate

## 2) Install dependencies (Django)

(venv_myknow) $ pip install -r requirements.txt 

## 3) Create the database

(venv_myknow) $ ./manage.py makemigrations  
(venv_myknow) $ ./manage.py migrate

## 4) Create an admin user

(venv_myknow) $ ./manage.py createsuperuser



-------------

# TEST

(venv_myknow should be activated, see above)


## 1) Automatic tests

(venv_myknow) $ ./manage.py test myknowapp


## 2) Manual testing with Django shell

(venv_myknow) $ ./manage.py shell

	>>> from django.contrib.auth.models import User
	>>> User.objects.all()
	<QuerySet [<User: epallier>]>
	>>> me = User.objects.get(username='epallier')
	>>> me
	<User: epallier>
	
	
	>>> from myknowapp.models import Entity
		
	>>> Entity.objects.filter(name__contains="ma")
	<QuerySet [<Entity: Mars>, <Entity: human body>, <Entity: Gamma ray>, <Entity: maliciousness>]>
	
	>>> from django.utils import timezone
	
	>>> Entity.objects.filter(date_created__lte=timezone.now())
	<QuerySet [<Entity: love>, <Entity: Earth>, <Entity: Mars>, <Entity: Venus>, <Entity: celestial body>, <Entity: Sun>, <Entity: fear>, <Entity: vehicle>, <Entity: wheel>, <Entity: volant>, <Entity: car>, <Entity: star>, <Entity: Saturn>, <Entity: Mercury>, <Entity: Jupiter>, <Entity: Uranus>, <Entity: Neptune>, <Entity: planet>, <Entity: stellar system>, <Entity: galaxy>, '...(remaining elements truncated)...']>
	
	>>> Entity.objects.filter(date_updated__lte=timezone.now())
	<QuerySet [<Entity: love>, <Entity: Earth>, <Entity: Mars>, <Entity: Venus>, <Entity: celestial body>, <Entity: Sun>, <Entity: fear>, <Entity: vehicle>, <Entity: wheel>, <Entity: volant>, <Entity: car>, <Entity: star>, <Entity: Saturn>, <Entity: Mercury>, <Entity: Jupiter>, <Entity: Uranus>, <Entity: Neptune>, <Entity: planet>, <Entity: stellar system>, <Entity: galaxy>, '...(remaining elements truncated)...']>
	>>> 
	
	>>> Entity.objects.order_by('date_created')
	<QuerySet [<Entity: love>, <Entity: Earth>, <Entity: Mars>, <Entity: Venus>, <Entity: celestial body>, <Entity: Sun>, <Entity: fear>, <Entity: vehicle>, <Entity: wheel>, <Entity: volant>, <Entity: car>, <Entity: star>, <Entity: Saturn>, <Entity: Mercury>, <Entity: Jupiter>, <Entity: Uranus>, <Entity: Neptune>, <Entity: planet>, <Entity: stellar system>, <Entity: galaxy>, '...(remaining elements truncated)...']>
	
	>>> Entity.objects.order_by('-date_created')
	<QuerySet [<Entity: Enceladus>, <Entity: Titan>, <Entity: Moon>, <Entity: maliciousness>, <Entity: impatience>, <Entity: fruit of the Spirit>, <Entity: self-control>, <Entity: gentleness>, <Entity: faithfulness>, <Entity: goodness>, <Entity: patience>, <Entity: peace>, <Entity: joy>, <Entity: hate>, <Entity: kindness>, <Entity: benevolence>, <Entity: affection>, <Entity: Gamma ray>, <Entity: X-ray>, <Entity: Ultraviolet>, '...(remaining elements truncated)...']>
	
	>>> ss = Entity.objects.get(name='solar system')
	<Entity: solar system>
	>>> ss.name
	'solar system'
	>>> ss.abbr

	>>> ss.has_components.all()
	<QuerySet [<Entity: Sun>, <Entity: Mercury>, <Entity: Venus>, <Entity: Earth>, <Entity: Mars>, <Entity: Jupiter>, <Entity: Saturn>, <Entity: Uranus>, <Entity: Neptune>]>
	
	>>> ss.compounds.all()
	<QuerySet []>
	
	>>> ss.components.all()
	<QuerySet [<EntityHasComponent: EntityHasComponent object (6)>, <EntityHasComponent: EntityHasComponent object (7)>, <EntityHasComponent: EntityHasComponent object (8)>, <EntityHasComponent: EntityHasComponent object (9)>, <EntityHasComponent: EntityHasComponent object (10)>, <EntityHasComponent: EntityHasComponent object (11)>, <EntityHasComponent: EntityHasComponent object (12)>, <EntityHasComponent: EntityHasComponent object (13)>, <EntityHasComponent: EntityHasComponent object (14)>]>
	
	>>> ss.components.all()[0]
	<EntityHasComponent: EntityHasComponent object (6)>
	
	>>> ss.components.all()[0].component
	<Entity: Sun>
	>>> ss.components.all()[0].compound
	<Entity: solar system>
	
	>>> ss.components.all()[1].component
	<Entity: Mercury>
	>>> ss.components.all()[1].compound
	<Entity: solar system>
	
	>>> mars = Entity.objects.get(name='Mars')
	>>> mars.components.all()
	<QuerySet []>
	>>> mars.compounds.all()
	<QuerySet [<EntityHasComponent: EntityHasComponent object (10)>]>
	>>> mars.compounds.all()[0].component
	<Entity: Mars>
	>>> mars.compounds.all()[0].compound
	<Entity: solar system>
	>>> mars.compounds.all()[0].qty
	1
	
	>>> from myknowapp.models import Entity
	>>> Entity.objects.first()
	<Entity: love>
	>>> e = Entity.objects.first()
	>>> e.name
	'love'
	>>> e.components.all()
	<QuerySet []>
	>>> e.synonyms.all()
	<QuerySet [<Entity: affection>, <Entity: benevolence>, <Entity: kindness>]>
	>>> e.synonyms.first()
	<Entity: affection>



-------------

# RUN

(venv_myknow should be activated, see above)

## 1) Start web server

(venv_myknow) $ ./manage.py runserver

## 2) Go to myknow website

Connect to http://localhost:8000  
From this webpage, there is a link "=> GO TO ADMIN SITE" to go to the ADMIN site in order to enter some entities into the database.  
You can also go directly there:  
Connect to http://localhost:8000/admin  
Login as the admin user (created at step 4 above)

