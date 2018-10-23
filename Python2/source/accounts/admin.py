from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import User

class CustomUserAdmin(UserAdmin):
    '''
    Custom User Admin class
    '''
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        (_('Personal Info'), {
            'fields': ('first_name', 'last_name')
        }),
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_staff',
            )
        }),
    )

    change_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', ),
        }),
        (_('Personal Info'), {
            'fields': (('first_name', 'last_name')
        }),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2')
        }),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name')
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', )
        }),
    )

    readonly_fields = ('email', 'is_superuser', )

    list_display = ('email', 'first_name', 'last_name', 'is_active')

    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('first_name', )
    list_filter = ('is_active', )
    list_per_page = 50

    actions = ['activate', 'deactivate']

    def deactivate(self, request, queryset):
        queryset.update(is_active=False)

    deactivate.short_description = "Deactivate selected users"

    def activate(self, request, queryset):
        queryset.update(is_active=True)

    activate.short_description = "Activate selected users"

    @staticmethod
    def has_delete_permission(request, obj=None):
        return False

    def get_queryset(self, request):
        qs = super(CustomUserAdmin, self).get_queryset(request)
        qs = qs.filter(is_superuser=False)
        return qs


admin.site.register(User, CustomUserAdmin)

admin.site.unregister(Group)
