from django.db import models

# Create your models here.
# En mi_app/models.py

from django.db import models

class Clase1(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.IntegerField()

class Clase2(Clase1):
    campo3 = models.TextField()

class Clase3(models.Model):
    campo4 = models.CharField(max_length=50)
    campo5 = models.EmailField()
