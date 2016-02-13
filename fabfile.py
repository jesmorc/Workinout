from fabric.api import run, local, hosts, cd
from fabric.contrib import django


#Descargar la app
def getApp():
	run('sudo apt-get update')
	run('sudo apt-get install -y git')
	run('sudo rm -rf Workinout/')
	run('sudo git clone https://github.com/jesmorc/Workinout.git')

#Instalar la app
def install():
	run('cd Workinout/ && sudo make install')

#Ejecucion de test
def test():
	run('cd Workinout/ && make test')

#Ejecucion de la aplicacion
def runApp():
	run('sudo python Workinout/manage.py runserver 0.0.0.0:80')
	#run('cd Workinout/ && make run')
	
#Crea la maquina en azure
def crearMaquina():
	run('cd Workinout/ && make crearMaquina')

#Provisiona la maquina en azure
def provisionarMaquina():
	run('cd Workinout/ && make provisionarMaquina')
