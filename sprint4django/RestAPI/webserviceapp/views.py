from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Tcanciones
from .models import Tcomentarios
from django.views.decorators.csrf import csrf_exempt
import json

def pagina_de_prueba(request):
	return HttpResponse("<h1>Hola k tal</h1>");

def devolver_canciones(request):
	cancioness = Tcanciones.objects.all();
	respuesta_final = [];
	for i in cancioness:
		diccionario = {}
		diccionario['id'] = i.id
		diccionario['titulo'] = i.nombre
		diccionario['fecha'] = i.fecha_publicacion
		diccionario['url'] = i.url_imagen
		diccionario['autores'] = i.autoria
		respuesta_final.append(diccionario)
	return JsonResponse(respuesta_final, safe=False)

def devolver_cancion_por_id(request, id_solicitado):
	cancion = Tcanciones.objects.get(id = id_solicitado)
	comentarios = cancion.tcomentarios_set.all()
	lista_comentarios = []
	for i in comentarios:
		diccionario = {}
		diccionario['id'] = i.id
		diccionario['comentario'] = i.comentario
		lista_comentarios.append(diccionario)
	resultado = {
		'id': cancion.id,
		'titulo': cancion.nombre,
		'fecha': cancion.fecha_publicacion,
		'url': cancion.url_imagen,
		'autores': cancion.autoria,
		'comentarios': lista_comentarios
	}
	return JsonResponse(resultado, json_dumps_params={'ensure_ascii': False})

@csrf_exempt
def guardar_comentario(request, cancion_id):
	if request.method != 'POST':
		return None
	
	json_peticion = json.loads(request.body)
	comentario = Tcomentarios()
	comentario.comentario = json_peticion['nuevo_comentario']
	comentario.cancion = Tcanciones.objects.get(id = cancion_id)
	comentario.save()
	return JsonResponse({"status": "ok"})
