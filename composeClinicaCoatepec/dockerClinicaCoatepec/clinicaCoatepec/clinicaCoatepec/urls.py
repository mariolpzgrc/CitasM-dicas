"""clinicaCoatepec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from clinicaCoatepec import views

urlpatterns = [
    path('citas/', views.citaMedica),
    path('citas/<int:pk>/', views.CitaMedica_detalle),
    path('paciente/', views.Paciente),
    path('paciente/<int:pk>/', views.Paciente_detalle),
    path('medico/', views.Medico)
    path('medico/<int:pk>/', views.Medico_detalle)
]
