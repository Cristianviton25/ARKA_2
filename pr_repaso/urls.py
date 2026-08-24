from django.contrib import admin
from django.urls import path, include
from . import views  # Importa la vista de la página principal

urlpatterns = [
    path('admin/', admin.site.urls),
    # Página principal directamente al entrar a la raíz del sitio
    path('', views.vista_principal, name='inicio_proyecto'),
    # URLs de la aplicación app_repaso
    path('', include('app_repaso.urls')),
]