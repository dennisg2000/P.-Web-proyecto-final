"""gas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
import trabajadores.views
import balones.views
import clientes.views
import proveedores.views

router = routers.DefaultRouter()
router.register(r'balones', balones.views.BalonViewSet)
router.register(r'clientes', clientes.views.ClienteViewSet)
router.register(r'proveedores', proveedores.views.ProveedorViewSet)
router.register(r'trabajadores', trabajadores.views.TrabajadoresViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path("api-auth/", include("rest_framework.urls"))
]
