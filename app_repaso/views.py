from django.shortcuts import render
from .models import Micurso  # Corregido sin espacios
from django.http import HttpResponse

def vista_app(request):
    return render(request, 'app_repaso/index.html')

def crear_curso(request):
    # Cambiamos el nombre de la variable a minúscula para no sobrescribir el modelo
    cursos_nuevos = [
        Micurso(instructor='Rider', competencia='HTML', ambiente='Adso1', aprendiz='Cristian'),
        Micurso(instructor='Henry', competencia='Requerimientos', ambiente='Adso2', aprendiz='Miguel'),
        Micurso(instructor='Edwin', competencia='Basedatos', ambiente='Adso3', aprendiz='Juan'),
    ]

    # Guardamos la lista en la base de datos masivamente
    Micurso.objects.bulk_create(cursos_nuevos)
    
    return HttpResponse("Mi Curso creado exitosamente.")

def listar_curso(request):
    cursos = Micurso.objects.all()
    
    return render (request, 'crear_cursos.html', {'Micurso' :cursos})