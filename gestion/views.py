from rest_framework import viewsets
from .models import Departamento, Municipio, Coordenada, Brigada, Parcela, ConteoArbol
from .serializers import (
    DepartamentoSerializer, MunicipioSerializer, CoordenadaSerializer,
    BrigadaSerializer, ParcelaSerializer, ConteoArbolSerializer
)

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('dashboard')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def dashboard(request):
    return render(request, 'gestion/dashboard.html')


from django.shortcuts import render, redirect
from .models import Brigada
from django.contrib.auth.decorators import login_required


from django.shortcuts import render
from .models import Brigada, Coordenada

def crear_brigada(request):
    brigada_creada = None
    coordenadas_disponibles = Coordenada.objects.all()

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        estado = request.POST.get('estado')
        coord_id = request.POST.get('coordenada')

        coordenada = Coordenada.objects.get(id=coord_id) if coord_id else None

        brigada_creada = Brigada.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            estado=estado,
            coordenadas=coordenada
        )

    brigadas = Brigada.objects.all().order_by('-fecha_creacion')

    return render(request, 'gestion/crear_brigada.html', {
        'brigada': brigada_creada,
        'brigadas': brigadas,
        'coordenadas': coordenadas_disponibles
    })





from django.contrib.auth.models import User
from .models import Brigada


from django.contrib.auth import get_user_model
User = get_user_model()

from django.shortcuts import render
from .models import Brigada
from .services import obtener_usuarios_no_admin

def asignar_miembros(request):
    brigadas = Brigada.objects.all()
    empleados = obtener_usuarios_no_admin()

    return render(request, "gestion/asignar_miembros.html", {
        "brigadas": brigadas,
        "empleados": empleados
    })




def crear_coordenadas(request):
    if request.method == 'POST':
        lat = request.POST.get('latitud')
        lng = request.POST.get('longitud')
        dep_nombre = request.POST.get('departamento')
        mun_nombre = request.POST.get('municipio')

        if lat and lng and dep_nombre and mun_nombre:
            # Obtener o crear el departamento
            departamento, _ = Departamento.objects.get_or_create(nombre=dep_nombre)

            # Obtener o crear el municipio asociado a ese departamento
            municipio, _ = Municipio.objects.get_or_create(nombre=mun_nombre, departamento=departamento)

            # Guardar la coordenada
            Coordenada.objects.create(
                latitud=lat,
                longitud=lng,
                departamento=departamento,
                municipio=municipio
            )

            return redirect('dashboard')

    return render(request, 'gestion/crear_coordenadas.html')





from django.db.models import Prefetch
from django.contrib.auth.models import User


def reportes(request):
    coordenadas = Coordenada.objects.select_related('departamento', 'municipio')
    brigadas = Brigada.objects.prefetch_related('miembros')
    
    return render(request, 'gestion/reportes.html', {
        'coordenadas': coordenadas,
        'brigadas': brigadas,
    })

from django.shortcuts import render

def ver_notificaciones(request):
    return render(request, 'gestion/ver_notificaciones.html')  # crea esta plantilla también

def registro_campo(request):
    return render(request, 'gestion/registro_campo.html')  # crea esta plantilla también

def reporte_brigada(request):
    return render(request, 'gestion/reporte_brigada.html')  # crea esta plantilla también


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer

class CoordenadaViewSet(viewsets.ModelViewSet):
    queryset = Coordenada.objects.all()
    serializer_class = CoordenadaSerializer

class BrigadaViewSet(viewsets.ModelViewSet):
    queryset = Brigada.objects.all()
    serializer_class = BrigadaSerializer

class ParcelaViewSet(viewsets.ModelViewSet):
    queryset = Parcela.objects.all()
    serializer_class = ParcelaSerializer

class ConteoArbolViewSet(viewsets.ModelViewSet):
    queryset = ConteoArbol.objects.all()
    serializer_class = ConteoArbolSerializer
