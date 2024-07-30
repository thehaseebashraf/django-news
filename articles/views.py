from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article
from .mixins import AdminRequiredMixin
from .forms import CommentForm, TicketForm
from django.shortcuts import redirect
from django.views import View

# View for listing all tickets
class TicketListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "ticket_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticket_count'] = Article.objects.count()
        return context
    
    
# View for displaying ticket details and handling comment form submissions
class TicketDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "ticket_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()  # Add the comment form to the context
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = self.object
            comment.author = request.user  # Set the author to the currently logged-in user
            comment.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse("article_detail", kwargs={"pk": self.object.pk})

# View for updating tickets
class TicketUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ("title", "description")
    template_name = "ticket_edit.html"

# View for deleting tickets, restricted to admins
class TicketDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Article
    template_name = "ticket_delete.html"
    success_url = reverse_lazy("article_list")

# View for creating new tickets
class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = TicketForm
    template_name = 'ticket_new.html'
    success_url = reverse_lazy('article_list')  # Redirect to the article list after creation

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the current user
        return super().form_valid(form)
