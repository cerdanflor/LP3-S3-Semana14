from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Articulo
from django.db.models import Q

# Create your views here.

layout = """

"""

def index(request):
    estudiantes = [ 'Isabella Caballero',
                    'Alejandro Hermitaño', 
                    'Joan Palomino', 
                    'Pierre Bernaola', 
                    'Fabricio Condori', 
                    'GiamPierre Huamán' ]
    return render(request,'index.html',{
        'titulo': 'Inicio',
        'mensaje': 'Proyecto Web con DJango (Desde el View)',
        'estudiantes': estudiantes
    })

def saludo(request):
    return render(request,'saludo.html',{
        'titulo': 'Saludo',
        'autor_saludo': 'Mg. Flor Elizabeth Cerdán León' 
    })

def rango(request):
   a = 10
   b = 20
   rango_numeros = range(a,b+1)
   return render(request,'rango.html',{
        'titulo': 'Rango',
        'a': a,
        'b': b,
        'rango_numeros': rango_numeros 
    })

def rango2(request,a=0,b=100):
    if a>b:
        return redirect('rango2',a=b, b=a)

    resultado = f"""
        <h2> Numeros de [{a},{b}] </h2>
        Resultado: <br>
        <ul> 
    """
    
    while a<=b:
        resultado +=  f"<li> {a} </li>"
        a+=1
    resultado += "</ul"
    return HttpResponse(layout + resultado)

def crear_articulo(request, titulo, contenido, publicado):
    articulo = Articulo(
        titulo = titulo,
        contenido = contenido,
        publicado = publicado
    )
    articulo.save()
    return HttpResponse(f"Articulo Creado: {articulo.titulo} - {articulo.contenido}")

def buscar_articulo(request):
    try:
        articulo = Articulo.objects.get(id=6)
        resultado = f"Articulo: <br>ID:{articulo.id} <br>Título: {articulo.titulo} <br>Contenido: {articulo.contenido}" 
    except:
        resultado: "<h1> Articulo No Encontrado </h1>"
    return HttpResponse(resultado)

def editar_articulo(request, id):
    articulo = Articulo.objects.get(pk=id)

    articulo.titulo = "Enseñanza OnLine en la Untels"
    articulo.contenido = "Aula Virtual. Google Meet. Portal Académico. Correo Institucional"
    articulo.publicado = False

    articulo.save()
    return HttpResponse(f"Articulo Editado:  <br>ID:{articulo.id} <br>Nuevo Título: {articulo.titulo} <br>Nuevo Contenido: {articulo.contenido}")

def listar_articulos(request):
    #articulos = Articulo.objects.all()    
    articulos = Articulo.objects.filter(
        Q(titulo__contains="Java") | Q(titulo__contains="PHP")    
    )
    return render(request,'listar_articulos.html',{
        'articulos': articulos,
        'titulo': 'Listado de Articulos'
    })

def eliminar_articulo(request, id):
    articulo = Articulo.objects.get(pk=id)
    articulo.delete()
    return redirect('listar_articulos')


def save_articulo(request):
    articulo = Articulo(
        titulo = titulo,
        contenido = contenido,
        publicado = publicado
    )
    articulo.save()
    return HttpResponse(f"Articulo Creado: {articulo.titulo} - {articulo.contenido}")

def create_articulo(request):
    return render(request, 'create_articulo.html')
