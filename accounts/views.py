# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from .models import CustomUser




class SignUpView(CreateView):
    form_class = CustomUserCreationForm 
    success_url = reverse_lazy('login') 
    template_name = "registration/signup.html"
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_admin = form.cleaned_data.get('is_admin')
        user.save()
        return super().form_valid(form)




