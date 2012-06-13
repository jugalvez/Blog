from django.forms import ModelForm
from blog.models import Comentario

class ComentarioForm(ModelForm):
	class Meta:
		model = Comentario
		exclude = ('articulo')