from django.contrib import admin
from members.models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ("user", "title")

admin.site.register(Member, MemberAdmin)

# Register your models here.
