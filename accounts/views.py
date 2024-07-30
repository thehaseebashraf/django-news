from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView,  DeleteView
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User


class SignUpView(CreateView):
    form_class = CustomUserCreationForm  # Form used for user registration
    success_url = reverse_lazy('login')  # URL to redirect after successful registration
    template_name = "registration/signup.html"  # Template used for rendering the sign-up form
    
    
    def form_valid(self, form):
        # Custom logic to save user data after form validation
        user = form.save(commit=False)  # Save form data to user object without committing to the database
        # user.is_admin = form.cleaned_data.get('is_admin')  # Set is_admin field from form data
        user.save()  # Save user object to the database
        return super().form_valid(form)  # Call parent class method to proceed with form validation


def check_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': CustomUser.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

def check_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': CustomUser.objects.filter(email__iexact=email).exists()
    }
    return JsonResponse(data)


def is_admin(user):
    return user.is_admin

@user_passes_test(is_admin)
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

# class UserCreateView(CreateView):
#     model = CustomUser
#     form_class = CustomUserCreationForm
#     template_name = 'users/user_form.html'
#     success_url = reverse_lazy('user_list')

# class UserUpdateView(UpdateView):
#     model = CustomUser
#     form_class = CustomUserChangeForm
#     template_name = 'users/user_form.html'
#     success_url = reverse_lazy('user_list')

@require_POST
@user_passes_test(is_admin)
def make_user_admin(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.is_admin = True
    user.save()
    return JsonResponse({'status': 'ok'})

@require_POST
@user_passes_test(is_admin)
def remove_user_admin(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.is_admin = False
    user.save()
    return JsonResponse({'status': 'ok'})

class UserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')
