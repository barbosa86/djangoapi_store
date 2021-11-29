from django.conf.urls import url
from StoresApp import views


urlpatterns= [
    url(r'^store$', views.storesApi),
    url(r'^store/([0-9]+)$', views.storesApi)
]