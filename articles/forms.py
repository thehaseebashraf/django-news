from django import forms
from .models import Comment

# Define a form for the Comment model
class CommentForm(forms.ModelForm):

    # Meta class to specify the model and fields to include in the form
    class Meta:
        model = Comment  # Specify the model to use
        fields = ("comment", "author")  # Specify the fields to include in the form
