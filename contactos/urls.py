from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_contactos, name='listar_contactos'),
    path('crear/', views.crear_contacto, name='crear_contacto'),
    path('editar/<int:id>/', views.editar_contacto, name='editar_contacto'),
    path('eliminar/<int:id>/', views.eliminar_contacto, name='eliminar_contacto'),
]
