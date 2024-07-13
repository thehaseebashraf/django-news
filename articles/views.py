from django.views.generic import ListView, DetailView, FormView
from django.urls import reverse_lazy, reverse
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article
from .mixins import AdminRequiredMixin
from .forms import CommentForm
from django.views import View

# View for listing all tickets
class TicketListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "ticket_list.html"

# View for displaying ticket details and a comment form
class CommentGet(DetailView):
    model = Article
    template_name = "ticket_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()  # Add the comment form to the context
        return context

# View for handling comment form submissions
class CommentPost(SingleObjectMixin, FormView):
    model = Article
    form_class = CommentForm
    template_name = "ticket_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object  # Associate the comment with the article
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        article = self.get_object()
        return reverse("article_detail", kwargs={"pk": article.pk})

# View for handling ticket details and comments, combining GET and POST methods
class TicketDetailView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

# View for updating tickets
class TicketUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = "ticket_edit.html"

# View for deleting tickets, restricted to admins
class TicketDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Article
    template_name = "ticket_delete.html"
    success_url = reverse_lazy("article_list")

# View for creating new tickets
class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "ticket_new.html"
    fields = (
        "title",
        "body",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the current user
        return super().form_valid(form)
