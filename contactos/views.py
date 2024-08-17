from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacto
from .forms import ContactoForm  # Asumiendo que tienes un formulario creado

def listar_contactos(request):
    contactos = Contacto.objects.all()
    return render(request, 'contactos/listar_contactos.html', {'contactos': contactos})
# Create your views here.

def crear_contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo contacto en la base de datos
            return redirect('listar_contactos')  # Redirige a la lista de contactos después de crear
    else:
        form = ContactoForm()

    return render(request, 'contactos/crear_contacto.html', {'form': form})

def editar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    if request.method == "POST":
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('listar_contactos')
    else:
        form = ContactoForm(instance=contacto)

    return render(request, 'contactos/editar_contacto.html', {'form': form})

def eliminar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    if request.method == "POST":
        contacto.delete()
        return redirect('listar_contactos')

    return render(request, 'contactos/eliminar_contacto.html', {'contacto': contacto})
