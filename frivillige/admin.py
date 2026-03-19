from django.contrib import admin
from .models import Volunteer


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at', 'availability')
    search_fields = ('first_name', 'last_name', 'email', 'phone', 'skills')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
