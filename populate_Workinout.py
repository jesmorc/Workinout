# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyectoP4.settings')

import django
django.setup()

from Workinout.models import Gym, Actividad


def populate():
	gymactividad = addGym(nombre="Yo10", lema="Relajate en nuestro spa", descripcion="Gym en el que hay de todo", direccion="calle camino ronda", visitas=0)
	addActividad(nombregym= gymactividad, titulo = "spinning", descripcion = "a pedalear un rato")
	addActividad(nombregym= gymactividad, titulo = "body pump", descripcion = "a mover ese body")
	addActividad(nombregym= gymactividad, titulo = "body combat", descripcion = "muevete y pelea")

	gymactividad = addGym(nombre="Vivagym", lema="Entrenamiento para todos los bolsillos",descripcion="Gym para todos los publicos y de gran espacio", direccion="Hipercor", visitas=0)
	addActividad(nombregym= gymactividad, titulo = "spinning", descripcion = "a pedalear un rato")
	addActividad(nombregym= gymactividad, titulo = "body pump", descripcion = "a mover ese body")
	addActividad(nombregym= gymactividad, titulo = "vivafit", descripcion = "alta intensidad")

	gymactividad = addGym("We", "Tu espacio deportivo", descripcion= "El más grande de Granada", direccion="La chana", visitas=0)
	addActividad(nombregym= gymactividad, titulo = "spinning", descripcion = "a pedalear un rato")
	addActividad(nombregym= gymactividad, titulo = "body pump", descripcion = "a mover ese body")
	addActividad(nombregym= gymactividad, titulo = "pilates", descripcion = "entrena y relajate")

    # Print out what we have added to the user.
	for b in Gym.objects.all():
		for t in Actividad.objects.filter(nombregym=b):
			print "- {0} - {1}".format(str(b), str(t))

def addActividad(nombregym, titulo, descripcion):
    p = Actividad.objects.get_or_create(nombregym=nombregym, titulo=titulo, descripcion= descripcion)[0]
    return p

def addGym(nombre, lema, descripcion, direccion, visitas):
    c = Gym.objects.get_or_create(nombre=nombre, lema=lema, descripcion=descripcion, direccion=direccion, visitas=visitas)[0]
    return c



# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()