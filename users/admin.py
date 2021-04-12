from django.contrib import admin
from django.contrib.auth import password_validation, get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import CustomUserCreationForm, CustomUserChangeForm

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    fieldsets = (
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'email', 'password')
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )

    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('email',)

    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'last_login', 'date_joined')
    readonly_fields = ('last_login', 'date_joined')


admin.site.register(User, CustomUserAdmin)
