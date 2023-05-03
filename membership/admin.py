from django.contrib import admin

from .models import Region, District, Registration, CustomUser


# Register the Region model in admin
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Specify the fields to display in the list view


# Register the District model in admin
@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'region')  # Specify the fields to display in the list view
    list_filter = ('region',)  # Add filters for the 'region' field


# Register the Registration model in admin
@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = (
        'reg_number', 'reg_date', 'region', 'district', 'branch')  # Specify the fields to display in the list view
    list_filter = ('region', 'district', 'branch')


@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display = ('nida',)  # Specify the fields to display in the list view
