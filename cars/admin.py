from django.contrib import admin
from cars.models import car, Brand

# Register your models here.
class carAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model',)  

class BrandAmin(admin.ModelAdmin):    
    list_display = ('name' ,)
    search_fields = ('name',)

admin.site.register(Brand, BrandAmin)
admin.site.register(car,carAdmin )
           
