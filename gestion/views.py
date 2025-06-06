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
    return redirect("http://localhost:8000/")  # ← dirección de tu login-service


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

from django.shortcuts import get_object_or_404, redirect

from .models import MiembroBrigada

def asignar_miembros(request):
    brigadas = Brigada.objects.all()
    empleados = obtener_usuarios_no_admin()

    if request.method == "POST":
        brigada_id = request.POST.get("brigada_id")
        miembros_ids = request.POST.getlist("miembros")
        brigada = get_object_or_404(Brigada, id=brigada_id)

        # Eliminar miembros anteriores
        MiembroBrigada.objects.filter(brigada=brigada).delete()

        # Buscar datos completos del usuario en la lista original
        for empleado in empleados:
            if str(empleado["id"]) in miembros_ids:
                MiembroBrigada.objects.create(
                    id_externo=empleado["id"],  # ✅ Esto es lo correcto
                    username=empleado["username"],
                    role=empleado["role"],
                    brigada=brigada
                )


        return redirect("asignar_miembros")

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


from .models import Brigada, MiembroBrigada

from django.shortcuts import render
from .models import Brigada, MiembroBrigada

def reportes(request):
    brigadas = Brigada.objects.all()
    datos_reporte = []

    for brigada in brigadas:
        miembros = MiembroBrigada.objects.filter(brigada=brigada)
        datos_reporte.append({
            "brigada": brigada,
            "miembros": miembros
        })

    return render(request, "gestion/reportes.html", {
        "datos_reporte": datos_reporte
    })




from django.shortcuts import render

from django.shortcuts import render
from .models import Brigada, MiembroBrigada
from django.db.models import Q

def ver_notificaciones(request):
    brigadas = Brigada.objects.all()
    datos_reporte = []

    for brigada in brigadas:
        miembros = MiembroBrigada.objects.filter(brigada=brigada)
        datos_reporte.append({
            "brigada": brigada,
            "miembros": miembros
        })

    return render(request, "gestion/ver_notificaciones.html", {
        "datos_reporte": datos_reporte
    })

from django.shortcuts import render, redirect
from .models import RegistroCampo, Brigada, Coordenada
from django.contrib import messages

def registro_campo(request):
    brigadas = Brigada.objects.all()
    coordenadas = Coordenada.objects.all()
    nuevo_registro = None

    if request.method == 'POST':
        brigada_id = request.POST.get('brigada')
        coordenada_id = request.POST.get('coordenada')
        condiciones = request.POST.get('condiciones_climaticas')
        equipo = request.POST.get('equipo_utilizado')
        observaciones = request.POST.get('observaciones')

        try:
            nuevo_registro = RegistroCampo.objects.create(
                brigada_id=brigada_id,
                coordenada_id=coordenada_id,
                condiciones_climaticas=condiciones,
                equipo_utilizado=equipo,
                observaciones=observaciones or '',
            )
            messages.success(request, "Registro guardado con éxito.")
            return redirect('registro_campo')
        except Exception as e:
            print("Error:", e)
            messages.error(request, f"No se pudo guardar: {str(e)}")

    registros = RegistroCampo.objects.all().order_by('-fecha')

    return render(request, 'gestion/registro_campo.html', {
        'brigadas': brigadas,
        'coordenadas': coordenadas,
        'registros': registros,
        'registro_guardado': nuevo_registro
    })

from .models import RegistroTecnico, RegistroBotanico

def registro_tecnico(request):
    brigadas = Brigada.objects.all()
    coordenadas = Coordenada.objects.all()
    nuevo = None

    if request.method == 'POST':
        nuevo = RegistroTecnico.objects.create(
            brigada_id=request.POST.get('brigada'),
            coordenada_id=request.POST.get('coordenada'),
            tipo_terreno=request.POST.get('tipo_terreno'),
            inclinacion=request.POST.get('inclinacion'),
            presencia_agua=bool(request.POST.get('presencia_agua')),
            estado_suelo=request.POST.get('estado_suelo'),
        )
        return redirect('registro_tecnico')

    registros = RegistroTecnico.objects.all().order_by('-fecha')
    return render(request, 'gestion/registro_tecnico.html', {
        'brigadas': brigadas,
        'coordenadas': coordenadas,
        'registros': registros,
        'registro_guardado': nuevo
    })

def registro_botanico(request):
    brigadas = Brigada.objects.all()
    coordenadas = Coordenada.objects.all()
    nuevo = None

    if request.method == 'POST':
        nuevo = RegistroBotanico.objects.create(
            brigada_id=request.POST.get('brigada'),
            coordenada_id=request.POST.get('coordenada'),
            especie_identificada=request.POST.get('especie_identificada'),
            familia_botanica=request.POST.get('familia_botanica'),
            estado_fenologico=request.POST.get('estado_fenologico'),
            observaciones=request.POST.get('observaciones', '')
        )
        return redirect('registro_botanico')

    registros = RegistroBotanico.objects.all().order_by('-fecha')
    return render(request, 'gestion/registro_botanico.html', {
        'brigadas': brigadas,
        'coordenadas': coordenadas,
        'registros': registros,
        'registro_guardado': nuevo
    })

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
