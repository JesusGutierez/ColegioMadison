from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('inicio/', views.inicio),
    path('descripcion/', views.descripcion),
    path('cursos/', views.cursos),
    path('contactanos/', views.contactanos)
]