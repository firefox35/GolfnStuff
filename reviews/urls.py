from django.urls import path
from .views import (index, about, AddReview, Reviews,
                    ReviewDetail, DeleteReview, EditReview)
from . import views

urlpatterns = [
    path("", index.as_view(), name="home"),
    path("about/", about.as_view(), name="about"),
    path("add_reviews/", AddReview.as_view(), name="add_review"),
    path("reviews/", Reviews.as_view(), name="reviews"),
    path("<slug:pk>/", ReviewDetail.as_view(), name="review_detail"),
    path("delete/<slug:pk>/", DeleteReview.as_view(), name="delete_review"),
    path("edit/<slug:pk>/", EditReview.as_view(), name="edit_review"),
]