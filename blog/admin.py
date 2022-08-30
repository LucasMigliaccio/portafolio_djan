from django.contrib import admin

from .models import *
from contacto.models import Contacto, Subscriptor
# Register your models here.

admin.site.register(Autor)

admin.site.register(Categoria)

admin.site.register(Post)

admin.site.register(Web)

admin.site.register(RedesSociales)


## CONTACTOAPP
admin.site.register(Contacto)

admin.site.register(Subscriptor)
