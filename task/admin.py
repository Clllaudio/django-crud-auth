from django.contrib import admin
from .models import Campana
# Register your models here.



class campanaAdmin (admin.ModelAdmin):
    readonly_fields = ("cumplida", )
    
admin.site.register(Campana, campanaAdmin)