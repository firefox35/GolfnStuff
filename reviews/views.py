from django.views.generic import (
    TemplateView, CreateView,
    ListView, DetailView,
    DeleteView, UpdateView)
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Review
from .forms import ReviewForm


"""View home screen"""


class index(TemplateView):
    template_name = "reviews/index.html"


"""View about list"""


class about(ListView):
    template_name = "reviews/about.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        return self.model.objects.all()[:3]


"""View all wines"""


class Reviews(ListView):
    template_name = "reviews/reviews.html"
    model = Review
    context_object_name = "reviews"
    form_class = ReviewForm
    success_url = "/reviews/"

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            reviews = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
        else:
            reviews = self.model.objects.all()
        return reviews


"""Add a Review"""


class ReviewDetail(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review
    context_object_name = "review"


"""Add Reviews"""


class AddReview(LoginRequiredMixin, CreateView):
    template_name = "reviews/add_review.html"
    model = Review
    context_object_name = "reviews"
    form_class = ReviewForm
    success_url = "/reviews/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddReview, self).form_valid(form)


"""Delete Reviews"""


class DeleteReview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = '/reviews/'

    def test_func(self):
        return self.request.user == self.get_object().user


"""Edit Reviews"""


class EditReview(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "reviews/edit_review.html"
    model = Review
    form_class = ReviewForm
    success_url = '/reviews/'

    def test_func(self):
        return self.request.user == self.get_object().user

