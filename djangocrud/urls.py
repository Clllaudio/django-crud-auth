"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from task import views


urlpatterns = [
    
    path('inicio/',views.inicio, name='inicio'),
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('campana/',views.campana, name='campana'),
    path('crear/campana/',views.crear_campana, name='crear_campana'),
    path('campana/<int:id_campana>/', views.detalle_campana, name='detalle_campana'),
    path('campana/<int:id_campana>/completada', views.campana_completada, name='campana_completada'),
    path('campana/<int:id_campana>/eliminada', views.campana_eliminada, name='campana_eliminada'),
    path('logout/',views.signout, name='logout')
    
] 
