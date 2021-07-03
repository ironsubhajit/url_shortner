from django.contrib import admin
from .models import Url, UserUrl

# Register your models here.
admin.site.register(Url)


@admin.register(UserUrl)
class UserUrlAdmin(admin.ModelAdmin):
    list_display = ['link', 'uuid', 'user']
