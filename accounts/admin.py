from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import Group

from unfold.admin import ModelAdmin
from unfold.contrib.filters.admin import BooleanRadioFilter
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

from .models import CustomUser

# for django unfold
# admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = [
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_superuser',
        'is_staff',
        'date_joined',
    ]
    list_display_links = ['username', 'email']
    list_filter = [
        ('is_staff', BooleanRadioFilter),
        ('is_superuser', BooleanRadioFilter),
        ('is_active', BooleanRadioFilter),
    ]
    list_filter_submit = True  #  add a submit button to the filter form
    readonly_fields = ['last_login', 'date_joined']
    show_full_result_count = False
    show_facets = admin.ShowFacets.NEVER


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    show_full_result_count = False
