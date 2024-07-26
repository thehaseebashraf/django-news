from django import forms
from .models import Article, Comment

# Define a form for the Article model (for creating and updating tickets)
class TicketForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'image']
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Upload Image',
        }

# Define a form for the Comment model (for adding comments to articles)
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text'] 
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Add a comment'})  
        }

