from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Articulo, Comentario
# Formulario de Comentarios
from blog.forms import ComentarioForm
from django.views.decorators.csrf import csrf_protect  
from django.shortcuts import render 



def index(request):
	posts = Articulo.objects.filter()[:5]
	return render_to_response('index.html', locals())

@csrf_protect
def articulo(request, id_art):
	post = Articulo.objects.get(id=id_art)
	comentarios = Comentario.objects.filter(articulo=post)

	if request.method == 'POST':
		comentario = Comentario(articulo=post)
		form = ComentarioForm(request.POST, instance=comentario)
		
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/articulo/{0}')
	else:
		form = ComentarioForm()

	return render(request, 'articulo.html', locals())