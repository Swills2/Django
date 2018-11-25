from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('reg',views.reg),
    path('log',views.log),
    path('info/<int:userID>',views.info),
    path('<int:userID>/logout',views.logout),
]