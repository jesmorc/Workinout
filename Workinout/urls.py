from django.conf.urls import patterns, url
from Workinout import views
from django.conf import settings


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^gym/(?P<gym_name_slug>\S+)$', views.gym, name='gym'),
        url(r'^add_gym/$', views.add_gym, name='add_gym'),
        url(r'^add_actividad/$', views.add_actividad, name='add_actividad'),
        url(r'^visitas/$', views.visitas, name='visitas'),
        url(r'^reclama_datos/$', views.reclama_datos, name='reclama_datos'),
        url(r'^megusta_actividad/$', views.megusta_actividad, name='megusta_actividad'),
       
        )
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )