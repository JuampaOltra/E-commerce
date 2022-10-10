from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages

from carro.carro import Carro
from tienda.models import Articulo, Proveedor
from .models import Usuario
from .forms import FormularioLogin, FormularioUsuario
from .mixins import LoginSuperUsuarioMixin, LoginProveedorUsuarioMixin

from datetime import datetime


# Create your views here.

class Inicio(TemplateView):

    template_name = 'layout.html'

    def inicio(self):
        carro = Carro(self.request)
        return carro


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carro'] = self.inicio()
        context['titulo'] = 'E-commerce'

        print('TITULO', context['titulo'])
        return context


class Login(FormView):
    template_name = 'usuarios/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('inicio')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('inicio')
                else:
                    messages.warning(request, 'No te has identidficado correctamente')
            return super(Login, self).dispatch(request, *args, **kwargs)


    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

def logout_user(request):
    logout(request)
    return redirect('login')



class ListadoUsuario(LoginSuperUsuarioMixin, ListView):
    model = Usuario
    template_name = 'usuarios/lista_usuarios.html'
    queryset = Usuario.objects.filter(is_active=True)

def proveedor(request):
    print(request.user.cif)
    data=[]
    if request.user:
        proveedor = Proveedor.objects.all()
        print(proveedor)
        for prov in proveedor:
            print('request',request.user.cif, 'prov',prov.nombre,prov.cif)
            if request.user.cif == prov.cif:
                print('ganador', prov.nombre)
                articulo=Articulo.objects.filter(proveedor=prov.id)
                for art in articulo:
                    data.append( [art.nombre,art.num_ventas, ])
                print(data)

                return render(request, 'proveedores/proveedores.html',{
                    'proveedor': proveedor,
                    'articulo':articulo,
                    'data':data
                    })


class RegistroUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = "usuarios/crear_usuario.html"
    success_url = reverse_lazy('login')