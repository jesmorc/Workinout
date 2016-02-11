## Despliegue en PaaS

El despliegue se ha realizado en el *PaaS* **Heroku**.

[![Heroku](https://www.herokucdn.com/deploy/button.png)](https://workinout.herokuapp.com/Workinout/)

El archivo de configuración para un correcto despliegue, aparte de tener los requisitos bien especificados en el *requirements.txt*, es el [Procfile]().


Para desplegar la app en Heroku, tecleamos en el terminal:
```
heroku create workinout
git push heroku master
```
Donde *workinout* es el nombre que le he puesto. (Si no se pasa parámetro pone un nombre por defecto).

Para visualizarla en el navegador:
```
heroku  ps:scale web=1
heroku open
```

No me funcionaba al principio y tuve que ejecutar este comando , sugerido por el propio texto de la excepción:
```
jesmorc@jesmorc-PClaptop ~/Workinout $ heroku config:set DISABLE_COLLECTSTATIC=1Setting config vars and restarting workinout... done
DISABLE_COLLECTSTATIC: 1
```

Para que funcione la aplicación con el modo ```DEBUG = false``` (explotación) he hecho las siguientes modificaciones en el archivo:

[settings.py](https://github.com/jesmorc/Workinout/blob/master/proyectoP4/settings.py):

```
STATIC_PATH = os.path.join(BASE_DIR, 'staticfiles')

Debug = False
ALLOWED_HOSTS = ['*']

```

