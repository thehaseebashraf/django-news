# articles/urls.py

from django.urls import path

# Importing the necessary views from the current directory
from .views import (
    TicketListView,
    TicketDeleteView,
    TicketDetailView,
    TicketCreateView,
    TicketUpdateView,
)

# Define the URL patterns for the 'articles' app
urlpatterns = [
    path("<int:pk>/", TicketDetailView.as_view(), name="article_detail"),  # URL pattern for viewing a specific article's details
    path("<int:pk>/edit/", TicketUpdateView.as_view(), name="article_edit"),  # URL pattern for editing a specific article
    path("<int:pk>/delete/", TicketDeleteView.as_view(), name="article_delete"),  # URL pattern for deleting a specific article
    path("new/", TicketCreateView.as_view(), name="article_new"),  # URL pattern for creating a new article
    path("", TicketListView.as_view(), name="article_list"),  # URL pattern for listing all articles
]
