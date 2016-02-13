## Despliegue automático

El despliegue se ha realizado con **Fabric** junto con **Azure**.

Ya hay una instancia de la app ejecutándose en [http://iv-jesmorc-ubuntuserver-service-euemq.cloudapp.net/Workinout/](http://iv-jesmorc-ubuntuserver-service-euemq.cloudapp.net/Workinout/).

Instalamos **Fabric** en local con:
```
sudo apt-get install fabric
```

Procedemos a crear el archivo [fabfile.py](https://github.com/jesmorc/Workinout/blob/master/fabfile.py), el cual especifica las acciones a realizar remotamente.

Para usarlo, ejecutamos en local:
```
fab -H vagrant@iv-jesmorc-ubuntuserver-service-euemq.cloudapp.net <nombre_funcion>
```
donde *nombre_funcion* es la función del **fabfile** a ejecutar.

Ejemplo usando la función *test*:

![prueba_fab](http://i.imgur.com/xkDgySn.png)
