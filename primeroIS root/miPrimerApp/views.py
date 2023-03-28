from django.shortcuts import render, HttpResponse
from .models import * # Decimos que de models vamos a importar todo lo que hay ahi

# Create your views here.
def index(request):
    """ return HttpResponse('Hola Mundo :)') # Regresa el response en la pantalla
        ~ Como definimos que cuando django quiera utilizar un template estuviese en la carpeta Templates, entonces podemos retornarlo tal cual (index.html)
        ~ get es para cuando sabemos que no hay repetidos y solo habra uno. En otro caso, usamos filter.
        ~ Para hacer una busqueda en la BD, los filtros se ponen como parametros en la variable que es deseada. Por ejemplo,
          si queremos todos los estudiantes del grupo 1, hacemos una variable grupo1 y en parametros ponemos grupo=1 (pues grupo es parte de la clase Estudiante).
        ~ el objeto recogido de la BD se puede devolver como objetos. 
        (en render)Se crea una variable y se referencía a la variable donde tenemos el obj. 
        Posterior a esto, veamos el index.html y añadimos la variable creada {{varEstudiante}} (por ejemplo), para observar el objeto en pantalla.
    """
    varGrupo1 = Estudiante.objects.filter(grupo=1)
    varGrupo4 = Estudiante.objects.filter(grupo=4)
    # Mismo apellido
    garces = Estudiante.objects.filter(apellidos="Garces")
    gomez = Estudiante.objects.filter(apellidos="Gómez")
    landaverde = Estudiante.objects.filter(apellidos="Landaverde")
    mendoza = Estudiante.objects.filter(apellidos="Mendoza")
    # Misma edad
    veinte = Estudiante.objects.filter(edad=20)
    veinteUno = Estudiante.objects.filter(edad=21)
    veinteDos = Estudiante.objects.filter(edad=22)
    veinteTres = Estudiante.objects.filter(edad=23)
    veinteCuatro = Estudiante.objects.filter(edad=24)
    veinteCinco = Estudiante.objects.filter(edad=25)
    # Grupo 3 y misma edad
    veinte3 = Estudiante.objects.filter(edad=20, grupo=3)
    veinteUno3 = Estudiante.objects.filter(edad=21, grupo=3)
    veinteDos3 = Estudiante.objects.filter(edad=22, grupo=3)
    veinteTres3 = Estudiante.objects.filter(edad=23, grupo=3)
    veinteCuatro3 = Estudiante.objects.filter(edad=24, grupo=3)
    veinteCinco3 = Estudiante.objects.filter(edad=25, grupo=3)
    varTodos = Estudiante.objects.filter()
    


    return render(request, 'index.html', {'varGrupo1':varGrupo1, 'varGrupo4':varGrupo4,
     'garces':garces, 'gomez':gomez, 'landaverde':landaverde, 'mendoza':mendoza, # Mismo apellido
     'veinte':veinte, 'veinteUno':veinteUno, 'veinteDos':veinteDos, 'veinteTres':veinteTres, 'veinteCuatro':veinteCuatro, 'veinteCinco':veinteCinco, # Misma edad
     'veinte3':veinte3, 'veinteUno3':veinteUno3, 'veinteDos3':veinteDos3, 'veinteTres3':veinteTres3, 'veinteCuatro3':veinteCuatro3, 'veinteCinco3':veinteCinco3, # Misma edad y grupo 3
      'varTodos':varTodos})