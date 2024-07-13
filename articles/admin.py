from django.contrib import admin
from .models import Article, Comment

# Inline class for comments within the article admin
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0  # Number of extra comment forms to display

# Article admin configuration
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,  # Include the CommentInline within the Article admin
    ]

# Register models with the admin site
admin.site.register(Article, ArticleAdmin)  # Register Article model with custom admin options
admin.site.register(Comment)  # Register Comment model with default admin options
