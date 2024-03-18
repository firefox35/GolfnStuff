from django.views.generic import (
    TemplateView, CreateView,
    ListView, DetailView,
    DeleteView, UpdateView)
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Review
from .forms import ReviewForm


class main(TemplateView):
    """View home screen"""
    template_name = "reviews/main.html"


class about(ListView):
    """View about list"""
    template_name = "reviews/about.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        return self.model.objects.all()[:3]


class reviews(ListView):
    """View all reviews"""
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


class review_detail(DetailView):
    """Add a Review"""
    template_name = "reviews/review_detail.html"
    model = Review
    context_object_name = "review"


class add_review(LoginRequiredMixin, CreateView):
    """Add Reviews"""
    template_name = "reviews/add_review.html"
    model = Review
    context_object_name = "reviews"
    form_class = ReviewForm
    success_url = "/reviews/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(add_review, self).form_valid(form)


class delete_review(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete Reviews"""
    model = Review
    success_url = '/reviews/'

    def test_func(self):
        return self.request.user == self.get_object().user


class edit_review(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit Reviews"""
    template_name = "reviews/edit_review.html"
    model = Review
    form_class = ReviewForm
    success_url = '/reviews/'

    def test_func(self):
        return self.request.user == self.get_object().user

