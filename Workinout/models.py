from django.db import models
from django.template.defaultfilters import slugify
import re




class Gym(models.Model):
    nombre = models.CharField(max_length=128, unique=True)
    lema = models.CharField(max_length=140)
    descripcion = models.TextField()
    direccion = models.CharField(max_length=192)
    visitas = models.IntegerField(default=0)
    slug = models.SlugField()
    logo = models.ImageField(upload_to='logos', blank=True)
    
    precio_boxeo = models.DecimalField(default=0, max_digits=3, decimal_places=1)
    precio_karate = models.DecimalField(default=0, max_digits=3, decimal_places=1)
    precio_judo = models.DecimalField(default=0, max_digits=3, decimal_places=1)


    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        #if self.id is None:
            #self.slug = slugify(self.name)
        self.slug = slugify(self.nombre)
        super(Gym, self).save(*args, **kwargs)

    def getNombre():
        return nombre

    
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.slug



class Actividad(models.Model):
    nombregym = models.ForeignKey(Gym) #nombre del gym, que es clave externa
    titulo = models.CharField(max_length=128)
    descripcion = models.CharField(max_length=256)
    megustas = models.IntegerField(default=0)
    
    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.titulo

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    # user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username