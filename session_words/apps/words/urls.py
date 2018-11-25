from django.urls import path
from . import views
urlpatterns = [
path('', views.index),
path('addwords', views.addwords),
path('clear', views.clear)
]