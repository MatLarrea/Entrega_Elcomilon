from django.contrib import admin
from .models import Servicio

# Register your models here.
class ServicioAdmin(admin.ModelAdmin):
    search_fields = ['titulo','contenido']
    list_filter = ['created', 'updated']
    date_hierarchy = "created"

    #Permite leer los campos invicibles
    readonly_fields =('created','updated')


admin.site.register(Servicio, ServicioAdmin)