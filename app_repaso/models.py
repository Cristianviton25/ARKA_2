from django.db import models

class Micurso(models.Model):
    instructor = models.CharField(max_length=255)
    competencia = models.CharField(max_length=100)
    ambiente = models.CharField(max_length=20)
    aprendiz = models.TextField()
    

