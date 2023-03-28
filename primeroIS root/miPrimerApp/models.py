from django.db import models

# Create your models here.

""" ~ Posterior a pegar ambas clases, hacemos dos comandos en terminal para las migraciones:
    python manage.py makemigrations
    python manage.py migrate

    ~ Posterior a tener copiados los archivos json de estudiante y grupo, ejecutamos los sig. comandos (esto para rellenar con datos la BD):
    python manage.py loaddata grupo.json
    python manage.py loaddata estudiante.json
"""
class  Grupo(models.Model):
    id_grupo  =  models.AutoField(primary_key=True)
    # Metodo toString
    def __str__(self):
        return f'{self.id_grupo}'

class  Estudiante(models.Model):
    numCta  =  models.IntegerField(default=0, max_length=9)
    nombres  =  models.CharField(max_length=200)
    apellidos  =  models.CharField(max_length=200)
    edad = models.IntegerField(default=0, max_length=3)
    # Cada estudiante guarda el grupo en el que está inscrito
    grupo  =  models.ForeignKey(Grupo, on_delete=models.SET_NULL, null=True)

    # Metodo toString
    def __str__(self):
        return f'Alumno: {self.nombres} {self.apellidos}, con número de cuenta {self.numCta}. Edad: {self.edad} años. Grupo: {self.grupo}'
