from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(
        User, related_name="contact_owner", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=False)
    email = models.EmailField(max_length=30, null=True, blank=False)
    phone = models.IntegerField()
    comment = models.TextField(max_length=2000, null=True, blank=False)

    def __str__(self):
        return self.name
