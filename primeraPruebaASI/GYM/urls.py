
from django.urls import path

from GYM import views

urlpatterns = [
    path('', views.saludo),
    
]