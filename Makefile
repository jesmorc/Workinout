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

crearMaquina:
	cd Workinout && sudo vagrant up --provider=azure

provisionarMaquina:
	cd Workinout && vagrant provision

azure:
	sudo vagrant provision
	fab -H vagrant@iv-jesmorc-ubuntuserver-service-euemq.cloudapp.net runApp