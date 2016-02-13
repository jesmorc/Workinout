install:
	sudo apt-get update
	sudo apt-get install -y python-dev
	sudo apt-get install -y python-pip
	sudo pip install --upgrade pip
	sudo pip install -r requirements.txt

test:
	python manage.py test
	
run:
	gunicorn proyectoP4.wsgi:application -b 0.0.0.0:80
