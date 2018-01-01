from django.contrib import admin
from apply.models import Status, Application


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("name", "ign", "position", "status")

admin.site.register(Application, ApplicationAdmin)
admin.site.register(Status)
