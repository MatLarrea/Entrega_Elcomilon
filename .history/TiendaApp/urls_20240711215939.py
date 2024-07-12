from django.urls import path
from . import views
from .views import agregar_categoria


urlpatterns = [
    path('', views.tienda, name="tienda"),
    path('agregar_categoria/', views.agregar_categoria, name='agregar_categoria'),
]