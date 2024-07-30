from django.urls import path
from .views import SignUpView, user_list, UserDeleteView, make_user_admin, remove_user_admin, check_username, check_email

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("users/", user_list, name="user_list"),
    path("ajax/check_username/", check_username, name="check_username"),
    path("ajax/check_email/", check_email, name="check_email"),
    path("users/<int:pk>/delete/", UserDeleteView.as_view(), name="user_delete"),
    path("users/<int:user_id>/make_admin/", make_user_admin, name="make_user_admin"),
    path("users/<int:user_id>/remove_admin/", remove_user_admin, name="remove_user_admin"),
]
