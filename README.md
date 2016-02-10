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



