from django.urls import path
from .views import HomePageView

# Define the URL patterns for the app
urlpatterns = [
    # Map the root URL to the HomePageView and name it 'home'
    path("", HomePageView.as_view(), name="home"),
]
