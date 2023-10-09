from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadatro'),
    path('login/', views.logar, name="logar"),
]
