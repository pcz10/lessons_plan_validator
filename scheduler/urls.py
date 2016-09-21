from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'generate/$', views.generate, name='generate'),
    url(r'data/$', views.data, name='data'),
    url(r'restrict/$', views.restrict, name='restrict'),
]
