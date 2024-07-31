# models.py
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=255)  # Title of the article
    description = models.TextField()  # Description content of the article
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Image for the article
    date = models.DateTimeField(auto_now_add=True)  # Date and time when the article is created
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,  # If the author is deleted, also delete their articles
    )

    def __str__(self):
        return self.title  # String representation of the Article model

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})  # URL to view the article details

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()  # Ensure this field exists
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text  # Ensure this field exists and is correctly referenced
    
# class Image(models.Model):
#     article = models.ForeignKey(Article, related_name='images', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='images/')