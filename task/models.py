from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Campana(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fechaInicio = models.DateTimeField(auto_now_add=True)
    fechaTermino = models.DateTimeField(null=True)
    cumplida = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=200)  

    def __str__(self):
        return self.titulo

