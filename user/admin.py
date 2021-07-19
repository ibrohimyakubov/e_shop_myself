from django.contrib import admin
from user.models import Profile


class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'image']


admin.site.register(Profile, UserAdmin)
