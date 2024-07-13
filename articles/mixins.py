from django.contrib.auth.mixins import UserPassesTestMixin

# A mixin to ensure the user is authenticated and is an admin
class AdminRequiredMixin(UserPassesTestMixin):
    
    # This method checks if the user is authenticated and is an admin
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin
