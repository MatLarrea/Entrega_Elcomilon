from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        #nos permite indicarle al modelo que esta son las forma de llamarlo en singular y en plural
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    #nos muestra el titulo del servicio al momento de visualizarlo en la base de datos admin
    def __str__(self):
        return self.nombre;

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="blog", null = True, blank= True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    #como en base de datos le indicamos a django que este modelo esta asociado a un usuario mediante su clave primaria y con la instruccion on_delete le indicamos que al momento de eliminar ese usuario todos sus post se eliminaran con el
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    #relación de muchos a muchos entre dos modelos
    categoria = models.ManyToManyField(Categoria)
    class Meta:
        #nos permite indicarle al modelo que esta son las forma de llamarlo en singular y en plural
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    #nos muestra el titulo del servicio al momento de visualizarlo en la base de datos admin
    def __str__(self):
        return '%s/%s' %(self.titulo,self.categoria);