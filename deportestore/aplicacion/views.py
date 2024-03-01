from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms      import AuthenticationForm
from django.contrib.auth            import authenticate, login
from django.contrib.auth.mixins     import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



# Create your views here.

def home(request):
    return render(request, "aplicacion/home.html")
@login_required
def productos(request):
    contexto = {'productos': Productos.objects.all()}
    return render(request, "aplicacion/productos.html", contexto)

@login_required
def medios_pago(request):
    contexto = {'medios_pago': Medios_pago.objects.all()}
    return render(request, "aplicacion/medios_pago.html", contexto)

@login_required
def sucursales(request):
    contexto = {'sucursales': Sucursales.objects.all()}
    return render(request, "aplicacion/sucursales.html", contexto)

@login_required
def preguntas_frecuentes(request):
    contexto = {'preguntas_frecuentes': Preguntas_frecuentes.objects.all()}
    return render(request, "aplicacion/preguntas_frecuentes.html", contexto)

@login_required
def productosForm(request):
    if request.method == "POST":
        miForm = ProductosForm(request.POST)
        if miForm.is_valid():
            producto_nombre = miForm.cleaned_data.get("nombre")
            precio_nombre = miForm.cleaned_data.get("precio")
            producto = Productos(nombre= producto_nombre, precio= precio_nombre)
            producto.save()
            return redirect(reverse_lazy('productos'))
    else:
      miForm = ProductosForm()
    return render(request, "aplicacion/productosForm.html", {"form": miForm})

@login_required
def medios_pagoForm(request):
    if request.method == "POST":
        miForm = Medios_pagoForm(request.POST)
        if miForm.is_valid():
            medios_pago_nombre = miForm.cleaned_data.get("nombre")
            medios_pago = Medios_pago(nombre= medios_pago_nombre)
            medios_pago.save()
            return render(request, "aplicacion/home.html")
    else:
      miForm = Medios_pagoForm()
    return render(request, "aplicacion/medios_pagoForm.html", {"form": miForm})

@login_required
def sucursalesForm(request):
    if request.method == "POST":
        miForm = SucursalesForm(request.POST)
        if miForm.is_valid():
            sucursales_ciudad = miForm.cleaned_data.get("ciudad")
            sucursales_direccion = miForm.cleaned_data.get("direccion")
            sucursales = Sucursales(ciudad= sucursales_ciudad, direccion= sucursales_direccion)
            sucursales.save()
            return render(request, "aplicacion/home.html")
    else:
      miForm = SucursalesForm()
    return render(request, "aplicacion/sucursalesForm.html", {"form": miForm})

@login_required
def buscar(request):
    return render(request, "aplicacion/buscar.html")

@login_required
def buscarProducto(request):
    if request.GET["buscar"]:
       patron = request.GET["buscar"]
       productos = Productos.objects.filter(nombre__icontains=patron)
       contexto = {"productos": productos}
       return render(request, "aplicacion/productos.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

@login_required
def updateproductos(request, id_productos):
    productos = Productos.objects.get(id=id_productos)
    if request.method == "POST":
        miForm = ProductosForm(request.POST)
        if miForm.is_valid():
            productos.nombre = miForm.cleaned_data.get('nombre')
            productos.precio = miForm.cleaned_data.get('precio')
            productos.save()
            return redirect(reverse_lazy('productos'))
    else:
      miForm = ProductosForm(initial={
          'nombre': productos.nombre,
          'precio': productos.precio,
      })
    return render(request, "aplicacion/productosForm.html", {"form": miForm})

@login_required
def deleteproductos(request, id_productos):
    productos = Productos.objects.get(id=id_productos)
    productos.delete()
    return redirect(reverse_lazy('productos'))

#____________________________________________________ Medios Pago
class Medios_pagoList(LoginRequiredMixin, ListView):
    model = Medios_pago

class Medios_pagoCreate(LoginRequiredMixin, CreateView):
    model = Medios_pago
    fields = ['nombre',]
    success_url = reverse_lazy('medios_pago')

class Medios_pagoUpdate(LoginRequiredMixin, UpdateView):
    model = Medios_pago
    fields = ['nombre',]
    success_url = reverse_lazy('medios_pago')

class Medios_pagoDelete(LoginRequiredMixin, DeleteView):
    model = Medios_pago
    success_url = reverse_lazy('medios_pago')

#_____________________________________________________ Sucursales
class SucursalesList(LoginRequiredMixin, ListView):
    model = Sucursales

class SucursalesCreate(LoginRequiredMixin, CreateView):
    model = Sucursales
    fields = ['ciudad', 'direccion']
    success_url = reverse_lazy('sucursales')

class SucursalesUpdate(LoginRequiredMixin, UpdateView):
    model = Sucursales
    fields = ['ciudad', 'direccion']
    success_url = reverse_lazy('sucursales')

class SucursalesDelete(LoginRequiredMixin, DeleteView):
    model = Sucursales
    success_url = reverse_lazy('sucursales')

#_____________________________________________________ Preguntas Frecuentes
class Preguntas_frecuentesList(LoginRequiredMixin, ListView):
    model = Preguntas_frecuentes

class Preguntas_frecuentesCreate(LoginRequiredMixin, CreateView):
    model = Preguntas_frecuentes
    fields = ['consulta',]
    success_url = reverse_lazy('preguntas_frecuentes')

class Preguntas_frecuentesUpdate(LoginRequiredMixin, UpdateView):
    model = Preguntas_frecuentes
    fields = ['consulta',]
    success_url = reverse_lazy('preguntas_frecuentes')

class Preguntas_frecuentesDelete(LoginRequiredMixin, DeleteView):
    model = Preguntas_frecuentes
    success_url = reverse_lazy('preguntas_frecuentes')

#______________________________________________________ Login, Registracion, Logout

def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)

            #____ Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            #__________________________________________

            return render(request, "aplicacion/home.html")
        else:
            return redirect(reverse_lazy('login'))
        
    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm })       

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))

    else:    
        miForm = RegistroForm()

    return render(request, "aplicacion/registro.html", {"form": miForm })


#_________________________________________________ Editar Perfil de Usuario

@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user = User.objects.get(username=usuario)
            user.email = informacion['email']
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.set_password(informacion['password1'])
            user.save()
            return render(request, "aplicacion/home.html")
    else:    
        form = UserEditForm(instance=usuario)

    return render(request, "aplicacion/editarPerfil.html", {"form": form })

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username=request.user)

            # ____ Para borrar el avatar viejo
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            # __________________________________
            avatar = Avatar(user=usuario, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # ___________ Hago una url de la imagen en request
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "aplicacion/home.html")

    else:    
        form = AvatarForm()

    return render(request, "aplicacion/agregarAvatar.html", {"form": form })
