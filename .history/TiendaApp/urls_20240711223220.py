from django.urls import path
from . import views
from .views import agregar_categoria


urlpatterns = [
    path('', views.tienda, name="tienda"),
    path('agregar_categoria/', views.agregar_categoria, name='agregar_categoria'),
    path('borrar_categoria/<int:categoria_id>/', views.borrar_categoria, name='borrar_categoria'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('borrar_producto/<int:producto_id>/', views.borrar_producto, name='borrar_producto'),
]