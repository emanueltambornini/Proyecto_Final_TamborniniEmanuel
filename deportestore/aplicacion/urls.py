from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),

    #_______________________________________________ Productos
    path('productos/', productos, name="productos"),
    path('productos_form/', productosForm, name="productos_form"),
    path('productos_actualizar/<id_productos>/', updateproductos, name="productos_actualizar"),
    path('productos_borrar/<id_productos>/', deleteproductos, name="productos_borrar"),

    #_________________________________________________ Medios Pago
    path('medios_pago/', Medios_pagoList.as_view(), name="medios_pago"),
    path('medios_pago_form/', Medios_pagoCreate.as_view(), name="medios_pago_form"),
    path('medios_pago_actualizar/<int:pk>/', Medios_pagoUpdate.as_view(), name="medios_pago_actualizar"),
    path('medios_pago_borrar/<int:pk>/', Medios_pagoDelete.as_view(), name="medios_pago_borrar"),

    #_______________________________________________ Sucursales
    path('sucursales/', SucursalesList.as_view(), name="sucursales"),
    path('sucursales_form/', SucursalesCreate.as_view(), name="sucursales_form"),
    path('sucursales_actualizar/<int:pk>/', SucursalesUpdate.as_view(), name="sucursales_actualizar"),
    path('sucursales_borrar/<int:pk>/', SucursalesDelete.as_view(), name="sucursales_borrar"),

    #_______________________________________________  Preguntas Frecuentes
    path('preguntas_frecuentes/', Preguntas_frecuentesList.as_view(), name="preguntas_frecuentes"),
    path('preguntas_frecuentes_form/', Preguntas_frecuentesCreate.as_view(), name="preguntas_frecuentes_form"),
    path('preguntas_frecuentes_actualizar/<int:pk>/', Preguntas_frecuentesUpdate.as_view(), name="preguntas_frecuentes_actualizar"),
    path('preguntas_frecuentes_borrar/<int:pk>/', Preguntas_frecuentesDelete.as_view(), name="preguntas_frecuentes_borrar"),


    #______________________________________________________ Login, Registracion, Logout

    path('login/', login_request, name="login"),
    path('registro/', register, name="registro"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),


    path('buscar/', buscar, name="buscar"),
    path('buscarproductos/', buscarProducto, name="buscarproductos"),

]