from django.db import models
from django.core.files.storage import FileSystemStorage
from Questionarios import settings
from mptt.models import MPTTModel, TreeForeignKey

class Tema(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='hijos')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Pregunta(models.Model):
    pregunta = models.TextField(max_length=500)
    archivo = models.FileField(upload_to='./preguntas_respuestas/', storage=FileSystemStorage(settings.STATIC_ROOT),null=True,blank=True)

    def __str__(self):
        return self.pregunta


class TemasPreguntas(models.Model):
    idtema = models.ForeignKey(Tema,on_delete=models.SET_NULL,null=True, blank=True)
    idpregunta = models.ForeignKey(Pregunta,on_delete=models.SET_NULL,null=True, blank=True)

    # def __str__(self):
    #     return self.pregunta

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='respuestas')
    respuesta = models.CharField(max_length=200)
    correctas = models.IntegerField(blank=True,null=True)


    def __str__(self):
        return self.respuesta