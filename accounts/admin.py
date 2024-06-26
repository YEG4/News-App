from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [ 'username','email', 'age', 'is_staff',]
    fieldsets = (
        (None, {
            "fields": (
                'age',
            ),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields' : ('age',)}))
    


admin.site.register(CustomUser, CustomUserAdmin)
