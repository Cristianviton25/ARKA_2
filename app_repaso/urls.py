from django.urls import path
from . import views

urlpatterns = [
    path('crear-curso/', views.crear_curso, name='crear_curso'),
    path('listar-curso/', views.listar_curso, name='listar_curso'),
    path('principal/', views.vista_app, name='vista_app'),
]