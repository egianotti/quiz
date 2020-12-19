from django.db import models
from django.core.files.storage import FileSystemStorage
from Questionarios import settings

# Create your models here.
class Temas(models.Model):
    titulo= models.CharField(max_length=250, null=True, blank=True)
    idpadre=models.IntegerField(null=True,blank=True)# 0,1,2,3,4,etc.

    def __str__(self):
        return self.titulo

class Pregunta(models.Model):

    pregunta = models.TextField(max_length=500)
    archivo = models.FileField(storage=FileSystemStorage(settings.STATIC_ROOT),null=True,blank=True)#,upload_to='./preguntas_respuestas/',)

    def __str__(self):
        return self.pregunta


class TemasPreguntas(models.Model):
    idtema = models.ForeignKey(Temas,on_delete=models.SET_NULL,null=True, blank=True)
    idpregunta = models.ForeignKey(Pregunta,on_delete=models.SET_NULL,null=True, blank=True)

    # def __str__(self):
    #     return self.pregunta

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='respuestas')
    respuesta = models.CharField(max_length=200)
    correctas = models.IntegerField(blank=True,null=True)


    def __str__(self):
        return self.respuesta
