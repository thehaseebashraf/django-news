from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Define a custom admin class for CustomUser model
class CustomUserAdmin(UserAdmin):
    # Use CustomUserCreationForm for adding new users
    add_form = CustomUserCreationForm
    # Use CustomUserChangeForm for updating existing users
    form = CustomUserChangeForm
    # Specify the model to be managed by this admin class
    model = CustomUser
    # Display these fields in the list view of admin interface
    list_display = [
        "email",
        "username",
        "age",
        "is_staff",
    ]
    # Extend fieldsets to include 'age' field in user detail view
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}),)
    # Extend add_fieldsets to include 'age' field when adding new user
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age",)}),)

# Register the CustomUser model with the CustomUserAdmin configuration
admin.site.register(CustomUser, CustomUserAdmin)
