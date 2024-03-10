from django.urls import path
from .views import (main, about, add_review, reviews,
                    review_detail, delete_review, edit_review)
from . import views

urlpatterns = [
    path("reviews/", main.as_view(), name="review"),
    path("about/", about.as_view(), name="about"),
    path("add_review/", add_review.as_view(), name="add_review"),
    path("reviews/", reviews.as_view(), name="reviews"),
    path("<slug:pk>", review_detail.as_view(), name="review_detail"),
    path("delete/<slug:pk>/", delete_review.as_view(), name="delete_review"),
    path("edit/<slug:pk>/", edit_review.as_view(), name="edit_review"),
]