from django.db import models
from blog.models import ModeloBase
# Create your models here.

class Contacto(ModeloBase):
    nombre= models.CharField("Nombre", max_length=150)
    apellido=models.CharField("Apellido", max_length=150)
    correo=models.EmailField("Correo Electrónico", max_length=150)
    asunto=models.CharField("Asunto", max_length=200)
    mensaje=models.TextField("Mensaje")

    class Meta:
        verbose_name= "Contacto"
        verbose_name_plural= "Contactos"

    def __str__(self):
        return self.asunto


class Subscriptor(ModeloBase):
    correo=models.EmailField("Correo Electrónico", max_length=150)
    
    class Meta:
        verbose_name= "Subscriptor"
        verbose_name_plural= "Subscriptores"
    
    def __str__(self):
        return self.correo