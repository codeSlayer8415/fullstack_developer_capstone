from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 2
    readonly_fields = ['manufacture_type']
# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['car_make','name','type','year']
    list_filter = ['car_make']
    readonly_fields = ['manufacture_type']
    # filtering based on car makers name
    search_fields = ['name', 'car_make__name']

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    search_fields = ['name']
    # now adding inline claases(i.e. one to many class)
    inlines = [CarModelInline]
# Register models here
admin.site.register(CarModel,CarModelAdmin)
admin.site.register(CarMake, CarMakeAdmin)