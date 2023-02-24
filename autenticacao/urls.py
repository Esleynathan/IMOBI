from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, nome="cadastro"),    
    path('logar/', views.logar, nome="logar"),
]
