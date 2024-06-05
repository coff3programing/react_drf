migrate:
	python manage.py migrate --settings=settings.local

migrations:
	python manage.py makemigrations --settings=settings.local

mrun: migrate
	python manage.py runserver --settings=settings.local

lrun:
	python manage.py runserver --settings=settings.local

prun:
	python manage.py runserver --settings=settings.prod
