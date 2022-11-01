from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm

user = get_user_model()


@admin.register(user)
class UserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')   # cюда мы добавили email, чтобы при регистрации в админке он был виден.
        }),
    )

    add_form = UserCreationForm