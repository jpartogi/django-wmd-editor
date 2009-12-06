from django.contrib import admin

from wmd.models import Config

class ConfigAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')

admin.site.register(Config, ConfigAdmin)