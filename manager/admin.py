# Django Libs:
from django.contrib import admin
# Local Libs:
from .models import Resource

admin.site.site_title = "MarsaMaroc Site Admin"
admin.site.site_header = "MarsaMaroc Administration"
class ResourceAdmin(admin.ModelAdmin):
    """Allow to edit Resource informations"""
    list_display = ('id', 'name', 'arrived_at',
                    'assigned_at', 'shift', 'merchandise')
    list_display_links = ('id', 'name')
    fieldsets = [
        ('General', {'fields': ['name', 'description']}),
        ('Dates', {'fields': ['arrived_at','assigned_at',]}),
        ('Content Type', {'fields': ['shift', 'merchandise']}),
        ('Position', {'fields': ['crane', 'tractor', 'elevator']}),
    ]

    list_filter = ('arrived_at', 'assigned_at', 'shift', 'merchandise')


admin.site.register(Resource, ResourceAdmin)
