## Despliegue en IaaS

El despliegue se ha realizado en el *IaaS* **Azure**.

[![Azure](http://azuredeploy.net/deploybutton.png)](http://iv-jesmorc-ubuntuserver-service-euemq.cloudapp.net/Workinout/

Instalamos las dependencias necesarias:
```
sudo apt-get install ruby-dev
sudo apt-get install nodejs-legacy
sudo apt-get install npm
sudo npm install -g azure-cli
```

Después instalamos el plugin de vagrant(>=1.6) para trabajar con azure con: 

```
vagrant plugin install vagrant-azure
```

Importo la cuenta de Azure y hago saber a Azure que la gestión de la cuenta hará desde mi host con:

```
azure login
azure account download
azure account import Azure\ Pass-1-15-2016-credentials.publishsettings
```

Generamos los certificados con:

```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout azurevagrant.key -out azurevagrant.key
chmod 600 ~/.ssh/azurevagrant.key
openssl x509 -inform pem -in azurevagrant.key -outform der -out azurevagrant.cer
```
Una vez creado el certificado, subimos el archivo ```.cer``` a Azure en la sección de *configuración - administración de certificados*.

Para poder autenticar Azure desde Vagrantfile es necesario crear un archivo .pem y concatenarle el archivo .key, para ello:

```
openssl req -x509 -key ~/.ssh/id_rsa -nodes -days 365 -newkey rsa:2048 -out azurevagrant.pem
cat azurevagrant.key > azurevagrant.pem
```

![subir certificado a azure]()

Instalamos Virtualbox con:

```
sudo apt-get install virtualbox virtualbox-dkms
```

Una vez hecho esto creamos el playbook de ansible [playbookej8.yml](https://github.com/AntonioPozo/Bares/blob/master/playbookej8.yml) que va a servir para todo lo relativo al aprovisionamiento de la aplicación:

- Actualizar el sistema
- Instalar herramientas necesarias
- Clonar el repositorio de Git
- Dar permisos necesarios
- **Ejecutar la aplicación**

Es necesario que el nombre del host sea ```localhost``` ya que el playbook se ejecutará en la máquina remota, que será la que proporcione el servicio. Como la máquina se ha creado con Vagrant, usaremos el usuario ```vagrant``` por defecto. 

Ahora creamos el [Vagrantfile]() que creará la máquina virtual en Azure. El último bloque del archivo hace uso del playbook de ansible.

Añadimos las líneas de abajo en el archivo ~/ansible_hosts

```
[localhost]
192.168.56.10
ansible_connection=local
```

Para curarme en salud, he añadido también el mísmo código en el archivo ```/etc/ansible/hosts``` ya que alguna vez he tenido problemas con ello.

Exportamos la variable de entorno de Ansible para que se reconozca el host:

```
export ANSIBLE_HOSTS=~/ansible_hosts 
```
Finalmente ejecutamos:

```
vagrant box add azure https://github.com/msopentech/vagrant-azure/raw/master/dummy.box
sudo vagrant up --provider=azure
```

La orden anterior crea la máquina, la configura y hace uso del playbook de ansible para desplegar la aplicación. 


Si sólo queremos hacer el último paso (porque la máquina está ya creada) ejecutamos:

```
vagrant provision
```

Captura de la aplicación funcionando en el host indicado en el campo ```azure.vm_name``` del Vagrantfile. En este caso:
```
azure.vm_name = 'iv-jesmorc-ubuntuserver' 
```

![deloyed_azure_app](http://i.imgur.com/FM8ZcUH.png)
