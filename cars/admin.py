from django.contrib import admin
from cars.models import Brand, Car, CarPhoto


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class PhotoCarInline(admin.TabularInline):
    model = CarPhoto
    extra = 1


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year',
                    'model_year', 'value', 'plate',)
    search_fields = ('model', 'brand',)
    inlines = [PhotoCarInline]


admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
