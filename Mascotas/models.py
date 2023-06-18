from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de Categoria")
    nombreCategoria = models.CharField(max_length=50, blank=True, verbose_name="Nombre de Categoria")

    def __str__(self):
        return self.nombreCategoria #permite acceder a los objetos a través de su nombre en el admin
    
    
class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=8, verbose_name="Codigo")
    marca= models.CharField(max_length=50, blank=True, verbose_name="Marca")
    tipo=models.CharField(max_length=50, blank=True, verbose_name="Tipo")
    imagen=models.ImageField(upload_to="imagenes",null=True, verbose_name='Imagen')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")

    def __str__(self):
        return self.codigo