from django.contrib import admin
from django.urls import path, include 

# List of URL patterns for the project
urlpatterns = [
    # URL pattern for the admin site
    path("admin/", admin.site.urls),

    # Include the accounts app URL configurations
    path("accounts/", include("accounts.urls")),

    # Include the default Django authentication URLs
    path("accounts/", include("django.contrib.auth.urls")),

    # Include the articles app URL configurations
    path("articles/", include("articles.urls")),

    # Include the pages app URL configurations for the homepage and other static pages
    path("", include("pages.urls")),
]
