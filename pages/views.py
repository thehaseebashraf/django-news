from django.views.generic import TemplateView

# Define a class-based view for the home page
class HomePageView(TemplateView): 
    # Specify the template to be used for rendering the home page
    template_name = "home.html"
