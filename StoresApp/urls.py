from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from StoresApp import views
from StoresApp.views import StoreViewSet

# ROTAS COM VIEW SET

store_list = StoreViewSet.as_view({'get': 'list', 'post': 'create'})
store_detail = StoreViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': ''})

urlpatterns = [
    path('stores/', store_list),
    path('stores/<int:pk>/', store_detail)
]

# Rotas com generic view 

# urlpatterns = [
#       path('stores/', views.StoreList.as_view()),
#       path(r'^stores/([0-9]+)$', views.StoresDetail.as_view())
# ] 