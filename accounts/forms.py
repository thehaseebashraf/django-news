from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # Additional field for signing up as admin
    is_admin = forms.BooleanField(required=False, label="Sign up as admin") 

    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
            "is_admin",  # Include the is_admin field in the form
        )

    def save(self, commit=True):
        # Override save method to include is_admin flag handling
        user = super().save(commit=False)  # Call the original save method
        is_admin = self.cleaned_data.get('is_admin')  # Get the value of is_admin from form data
        user.is_admin = is_admin  # Set the is_admin attribute of the user instance
        if commit:
            user.save()  # Save the user instance if commit is True
        return user  # Return the user instance
    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
        )
