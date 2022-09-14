"""authProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from authApp import views

urlpatterns = [

    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),

    path('user/', views.CrearUsuarioView.as_view()),
    path('user/<int:pk>/', views.DetalleUsuarioView.as_view()),

    path('Psalud/', views.CrearPersonalSaludView.as_view()),
    path('Psalud/<int:pk>/', views.DetallePersonalSaludView.as_view()),

    path('paciente/', views.CrearPacienteView.as_view()),
    path('paciente/<int:pk>/', views.DetallePacienteView.as_view()),

    path('familiar/', views.CrearFamiliarView.as_view()),
    path('familiar/<int:pk>/', views.DetalleFamiliarView.as_view()),
]
