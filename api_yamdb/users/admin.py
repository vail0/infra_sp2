from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    """Настройка отображения полей"""
    list_display = ('pk', 'username', 'email', 'role')
    list_editable = ('role',)
    verbose_name = 'Пользователи'
    list_filter = ('username',)
    readonly_fields = ('code',)
    search_fields = ('username', 'role')


admin.site.register(User, UserAdmin)
