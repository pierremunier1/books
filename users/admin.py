from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class MyUserAdmin(UserAdmin):

    model=UserAdmin.fieldsets

admin.site.register(CustomUser, MyUserAdmin)
