from django.apps import AppConfig

# Configuration class for the 'articles' app
class ArticlesConfig(AppConfig):
    
    # Define the default auto field for models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Specify the name of the app
    name = 'articles'
