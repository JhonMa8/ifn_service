from django.db import models
from django.contrib.auth.models import User

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.departamento})"

class Coordenada(models.Model):
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.latitud}, {self.longitud}"

from gestion.models import Coordenada  # Asegúrate de importar el modelo

class Brigada(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateField(auto_now_add=True)
    descripcion = models.TextField(blank=True, null=True)
    miembros = models.ManyToManyField(User, related_name="brigadas", blank=True)
    estado = models.CharField(max_length=20, choices=[
        ('activa', 'Activa'),
        ('inactiva', 'Inactiva'),
        ('en_misión', 'En misión')
    ], default='activa')

    coordenadas = models.ForeignKey(Coordenada, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

from django.db import models

class MiembroBrigada(models.Model):
    id_externo = models.IntegerField()
    username = models.CharField(max_length=150)
    role = models.CharField(max_length=50)
    brigada = models.ForeignKey(Brigada, on_delete=models.CASCADE, related_name="miembros_asignados")



class Parcela(models.Model):
    coordenada = models.ForeignKey(Coordenada, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=20)
    area_m2 = models.FloatField(default=3500)

    def __str__(self):
        return f"Parcela {self.codigo} - {self.coordenada}"

class ConteoArbol(models.Model):
    parcela = models.ForeignKey(Parcela, on_delete=models.CASCADE)
    especie = models.CharField(max_length=100)
    diametro_cm = models.FloatField()
    altura_m = models.FloatField()
    cantidad = models.PositiveIntegerField(default=1)
    fecha_recoleccion = models.DateField()
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.especie} x{self.cantidad} en {self.parcela}"

