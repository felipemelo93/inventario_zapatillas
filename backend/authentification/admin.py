from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin

from .models import User

class Usercustom(UserAdmin):
    model = User
    
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('nombre', 'apellido', 'local', 'estado')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('nombre', 'apellido', 'local', 'estado')}),
    )
    list_display = ('username', 'nombre', 'apellido', 'local', 'estado', 'is_staff', 'is_active')
    search_fields = ('username', 'nombre', 'apellido')
    ordering = ('username',)

admin.site.register(User,Usercustom)



