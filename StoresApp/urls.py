from django.conf.urls import url, urls
from django.urls.resolvers import URLPattern
from StoresApp import views



urlpatterns= [
    url(r'^store$', views.storesApi),
    url(r'^store/([0-9]+)$')
]