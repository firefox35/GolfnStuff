from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
import datetime


STATUS = ((0, "Draft"), (1, "Published"))

"""A model to create and manage reviews"""


class Review(models.Model):
    
    """A model to create and manage reviews"""
    user = models.ForeignKey(
        User, related_name="review_owner", on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=False, blank=False)
    product_name=models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(max_length=2000, null=False, blank=False)
    image = ResizedImageField(
        size=[400, 400], quality=75, upload_to='reviews/', force_format='WEBP',
        blank=False, null=False, default="")
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    posted_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-posted_on"]

    def __str__(self):
        return self.title
