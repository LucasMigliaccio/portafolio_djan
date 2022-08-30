from datetime import date
from django.db import models
import datetime


# Create your models here.

class Posts(models.Model):
    tittle=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to="proyectos/images")
    date=models.DateField(datetime.date.today)
