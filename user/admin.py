from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('staff', 'address', 'phone')

# Register your models here.
admin.site.register(Profile,ProfileAdmin)

