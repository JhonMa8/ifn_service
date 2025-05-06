from django.urls import include, path
from rest_framework import routers
from . import views

# Rutas para la API REST
router = routers.DefaultRouter()
router.register(r'departamentos', views.DepartamentoViewSet)
router.register(r'municipios', views.MunicipioViewSet)
router.register(r'coordenadas', views.CoordenadaViewSet)
router.register(r'brigadas', views.BrigadaViewSet)
router.register(r'parcelas', views.ParcelaViewSet)
router.register(r'conteo', views.ConteoArbolViewSet)

# Rutas para vistas HTML
urlpatterns = [
    path('api/', include(router.urls)),  # rutas de API
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('crear-brigada/', views.crear_brigada, name='crear_brigada'),
    path('asignar-miembros/', views.asignar_miembros, name='asignar_miembros'),
    path('crear-coordenadas/', views.crear_coordenadas, name='crear_coordenadas'),
    path('reportes/', views.reportes, name='reportes'),
    path('ver-notificaciones/', views.ver_notificaciones, name='ver_notificaciones'),
    path('registro-campo/', views.registro_campo, name='registro_campo'),
    path('reporte-brigada/', views.reporte_brigada, name='reporte_brigada'),
]
