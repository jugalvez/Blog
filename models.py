from django.db import models

class Articulo(models.Model):
	titulo = models.CharField(max_length=100, unique=True)
	cuerpo = models.TextField()
	fecha_entrada = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.titulo

class Comentario(models.Model):
	nombre = models.CharField(max_length=50)
	email = models.EmailField()
	texto = models.TextField()
	fecha_entrada = models.DateField(auto_now_add=True)
	# Llave externa del modelo Articulo
	articulo = models.ForeignKey(Articulo)

	def __unicode__(self):
		return self.nombre

