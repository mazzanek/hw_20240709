from django.contrib import admin
from .models import add_view

class add_viewAdmin(admin.ModelAdmin):
  list_display = ("rest_name", "rest_spec", "rest_address", "rest_website", "rest_phone")

# Register your models here.
admin.site.register(add_view, add_viewAdmin)