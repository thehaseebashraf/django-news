from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from .models import CustomUser



class SignUpView(CreateView):
    form_class = CustomUserCreationForm  # Form used for user registration
    success_url = reverse_lazy('login')  # URL to redirect after successful registration
    template_name = "registration/signup.html"  # Template used for rendering the sign-up form
    
    
    def form_valid(self, form):
        # Custom logic to save user data after form validation
        user = form.save(commit=False)  # Save form data to user object without committing to the database
        user.is_admin = form.cleaned_data.get('is_admin')  # Set is_admin field from form data
        user.save()  # Save user object to the database
        return super().form_valid(form)  # Call parent class method to proceed with form validation
