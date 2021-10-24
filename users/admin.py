from django.contrib import admin
from .models import UserAccount


class UserAccountAdmin(admin.ModelAdmin):
    list_display    = [
        'email','username','first_name','last_name','date_joined','is_staff','is_admin','is_superuser'
    ]
    readonly_fields = ['id','date_joined','last_login']
    search_fields   = ['email','username','first_name','last_name']
    #list_filter = ['']


admin.site.register(UserAccount, UserAccountAdmin)
