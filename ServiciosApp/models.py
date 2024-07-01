from django.db import models

# Create your models here

# Clase que corresponde a un servicio dentro de la página web
class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='servicios')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    #Meta nos permite definir una serie de carasteristicas al modelo
    class Meta:
        #nos permite indicarle al modelo que esta son las forma de llamarlo en singular y en plural
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    #nos muestra el titulo del servicio al momento de visualizarlo en la base de datos admin
    def __str__(self):
        return self.titulo;

