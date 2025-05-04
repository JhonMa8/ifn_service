"""
URL configuration for ifn_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from gestion import views as gviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestion.urls')),
    path('api/', include('gestion.urls')),
    path('dashboard/',        gviews.dashboard,                   name='dashboard'),
    path('crear-brigada/',    gviews.crear_brigada,               name='crear_brigada'),
    path('asignar-miembros/', gviews.asignar_miembros,            name='asignar_miembros'),
    path('crear-coordenadas/',gviews.crear_coordenadas,           name='crear_coordenadas'),
    
]




