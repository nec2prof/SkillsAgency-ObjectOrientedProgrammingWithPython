from app_cfp016 import views
from django.urls import path

urlpatterns = [
    path('', views.inicio, name='home'),  
    path('cursos', views.cursos, name='cursos'),
    path('profesores', views.profesores, name='profesores'), 
    path('estudiantes', views.estudiantes, name='estudiantes'),
    path('entregables', views.entregables, name='entregables')	
]