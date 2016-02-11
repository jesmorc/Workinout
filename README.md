# Workinout

Portal de gimnasios y actividades deportivas dentro de los mismos.

Jesús García Godoy

## Introducción

El fin del proyecto no es la aplicación en sí, si no la creación de una infraestructura donde alojar y desplegar dicha aplicación. La aplicacición consiste en un portal de gimnasios, el cual detalla las actividades de cada uno de ellos, así como de los precios medios y calificaciones de cada unas de éstas.
Se permite el registro de usuarios. Algunas secciones sñolo están disponibles si el usuario está registrado.


## Infraestructura

Par la aplicación web necesitamos un soporte que ofrezca una infraestructura que cuente con un servidor web para desplegar la aplicación, en el cual ejecutarse. Usará la BBDD del servidor, en la que se almacenará la información necesaria para la aplicación.

La infraestructura que he utilizado en este proyecto me ha proporcionado varias opciones, como las máquinas virtuales que me proporciona la IaaS Azure.


## Herramientas

- Desarrollada en Django. (framework de Python)
- BBDD SQLite3.
- Bootstrap para el estilo de la app web.
- Travis para integración contínua.
- PaaS: Heroku
- IaaS: Azure
- Despliegue automático: Fabric

La herramienta de construcción que usa Django es manage.py, el cual permite ejecutar la aplicación así como realizar varias operaciones de control.


# Requerimientos

Instalación de dependencias (usa el archivo [requirements.txt](https://github.com/jesmorc/Workinout/blob/master/requirements.txt)) : 
```
sudo pip install -r requirements.txt
```

Para ejecutar la apliación:
```
python manage.py runserver
```

Puerto por defecto: 8000

Nota: se puede asignar otro puerto cualquiera que esté libre.
Ej-> Puerto 80: ``` sudo python manage.py runserver 0.0.0.0:80```

# Instalación local

Nos clonamos el repositorio con:
```
git clone https://github.com/jesmorc/Workinout.git
```

Una vez dentro de la carpeta, en caso de que no estuviera la BBDD creada se crearía y se llenaría de datos con estos dos comandos de la imagen:

![createBBDD](http://i.imgur.com/dyaSP72.png)

Ejecutamos la aplicación con el comando visto antes:
```
python manage.py runserver
```

Y entramos al navegador a la dirección http://127.0.0.1:8000/Workinout/


# Desarrollo basado en pruebas

Para el testeo,  Django dispone de *unittest*, utilizando un archivo [tests.py](https://github.com/jesmorc/Workinout/blob/master/Workinout/tests.py), que contiene los tests que queramos hacerle a la aplicación.

Los tests se ejecutan con: 
```
python manage.py test
```

![tests](http://i.imgur.com/bmclf7V.png)



