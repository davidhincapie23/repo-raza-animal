from django.shortcuts import render , get_object_or_404 , redirect
from .models import Animal
from .forms import AnimalForm
# Create your views here.

def index(request) :
    animals = Animal.objects.all()
    return render(
        request , 'animales/index.html' , 
        {
            'animals' : animals
        }
    )

def detalles_animal(request , id) :
    animal = get_object_or_404(Animal , pk = id) 

    return render(
        request , 'animales/detalles_animals.html' ,
        {
            'animal' : animal
        }
    )

def crear_nuevo_animal(request) :
    if request.method == "POST" :
        animal_form = AnimalForm(request.POST)
        if animal_form.is_valid() :
            animal_form.save()
            return redirect('index')
    else :
        animal_form = AnimalForm()

    return render(
        request , 'animales/crear_nuevo_animal.html' ,
        {
            'animal_form' : animal_form
        }
    )

    

def editar_animal(request , id) :
    animal = get_object_or_404(Animal , pk = id)

    if request.method == "POST" :
        animal_form = AnimalForm(request.POST , instance = animal) 
        if animal_form.is_valid() :
            animal_form.save()
            return redirect('index')
    else :
        animal_form = AnimalForm(instance = animal)

    return render(
        request , 'animales/editar_animals.html' ,
        {
            'animal_form' : animal_form
        }
    )

def eliminar_animal(request , id) :
    animal = get_object_or_404(Animal , pk = id)

    if animal :
        animal.delete()

    return redirect('index')
