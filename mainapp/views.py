from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
"""
def inicio(request):
    
    return render(request, 'layout.html',{
        'titulo':'E-commerce'
    })

def nosotros(request):

    return render(request, 'mainapp/nosotros.html',{
        'title':'Nosotros'
    })"""

"""
def register_page(request):

    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        register_form = RegisterForm()

        if request.method == 'POST':
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Te has registrado correctamente')

                return redirect('inicio')
        return render(request, 'users/register.html',{
            'title': 'Registro',
            'register_form': register_form
        })

"""
"""
def login_page(request):

    if request.user.is_authenticated:
        return redirect('inicio')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            cif = request.POST.get('cif')

            user = authenticate(request, username=username, password=password, cif=cif)
            if user is not None:
                login(request, user)
                return redirect ('inicio')
            else:
                messages.warning(request, 'No te has identidficado correctamente')

        return render(request, 'users/login.html',{
            'titulo': 'Identificate para poder comprar',
        })


"""