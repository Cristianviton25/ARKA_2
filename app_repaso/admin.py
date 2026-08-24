from django.contrib import admin
from .models import Micurso

@admin.register(Micurso)
class MicursoAdmin(admin.ModelAdmin):
    list_display = ('instructor', 'competencia', 'ambiente')