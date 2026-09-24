from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('crear_tarea', views.crear_tarea, name= 'crear_tarea'),
    path('ver_tarea/<int:tid>/', views.ver_tarea, name= 'ver_tarea'),
    path('editar_tarea/<int:tid>/', views.editar_tarea, name= 'editar_tarea'),
    path('eliminar_tarea/<int:tid>/', views.eliminar_tarea, name= 'eliminar_tarea'),
]