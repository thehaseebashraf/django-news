from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):
    is_admin = forms.BooleanField(required=False, label="Sign up as admin")  #new
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
            "is_admin",) #now
    #new function    
    def save(self, commit=True):
        user = super().save(commit=False)
        is_admin = self.cleaned_data.get('is_admin')
        user.is_admin = is_admin  # Set the is_admin flag
        if commit:
            user.save()
        return user
        
class CustomUserChangeForm(UserChangeForm): 
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
)