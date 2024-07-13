from django.conf import settings
from django.db import models
from django.urls import reverse

# Article model to store articles
class Article(models.Model):
    title = models.CharField(max_length=255)  # Title of the article
    body = models.TextField()  # Body content of the article
    date = models.DateTimeField(auto_now_add=True)  # Date and time when the article is created
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,  # If the author is deleted, also delete their articles
    )

    def __str__(self):
        return self.title  # String representation of the Article model

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})  # URL to view the article details


# Comment model to store comments on articles
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # Each comment is related to a specific article
    comment = models.CharField(max_length=140)  # The content of the comment
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,  # If the author is deleted, also delete their comments
    )

    def __str__(self):
        return self.comment  # String representation of the Comment model

    def get_absolute_url(self):
        return reverse("article_list")  # URL to redirect after submitting a comment
