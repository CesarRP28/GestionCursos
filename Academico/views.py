from django.shortcuts import render,redirect
from .models import Curso

# Create your views here.
def home(request):
    cursos = Curso.objects.all() #Select *from curso  #Descargo los cursos y lo meto en este objeto
    return render(request,'gestionCursos.html', {'cursos':cursos}) #Carga la plantilla pero a parte le pasa los cursos, los objetos van sin comillas


def registroCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['txtCredito']

    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect('/')  #Te redirecciona a una página específica

def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('/')

def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, 'edicionCurso.html', {'curso': curso})

def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['txtCredito']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    return redirect('/')