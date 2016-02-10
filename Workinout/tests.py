from django.test import TestCase
from Workinout.models import Actividad, Gym, UserProfile
from django.test import Client



class SiteTestCase(TestCase):	
	
	# Testear respuesta del index
	def test_index(self):
		response = self.client.get('/Workinout/')
		self.assertEqual(response.status_code, 200)

	# Testear respuesta del sitio visitas	
	def test_visitas(self):
		response = self.client.get('/Workinout/visitas/')
		self.assertEqual(response.status_code, 200)

	# Testear respuesta del sitio about 	
	def test_about(self):
		response = self.client.get('/Workinout/about/')
		self.assertEqual(response.status_code, 200)
	
	# Testear respuesta del sitio login 	
	def test_login(self):
		response = self.client.get('/Workinout/login/')
		self.assertEqual(response.status_code, 200)


class GymTestCase(TestCase):
	# Crear gym
	def setUp(self):
		Gym.objects.create(nombre = "Corner", lema = "Ven a entrenar a gusto", direccion = "San Geronimo", visitas = 0, descripcion = "Gym variado. Apuntate", precio_boxeo = 5, precio_karate = 2, precio_judo = 2)

	# Testear tupla nombre-lema	
	def test_Gym_Lema(self):
		gym = Gym.objects.get(nombre = "Corner")
		self.assertEqual(gym.lema, "Ven a entrenar a gusto")


class ActividadTestCase(TestCase):
	#Crear actividad spinning
	def setUp(self):
		actividad = Actividad.objects.create(titulo = "Spinning", megustas = 5, nombregym_id = 1)

	# Testear tupla 
	def test_Actividad_Megustas(self):
		actividad = Actividad.objects.get(titulo = "Spinning")
		self.assertEqual(actividad.megustas, 5)