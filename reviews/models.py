from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
import datetime


STATUS = ((0, "Draft"), (1, "Published"))

"""A model to create and manage wines"""


class Review(models.Model):
    
    TYPE_OF_ITEM = (
        ("irons", "Irons"),
        ("drivers", "Drivers"),
        ("woods", "Woods"),
        ("putters", "Putters"),
        ("wedges", "Wedges"),
        ("shirts", "Shirts"),
        ("tops", "Tops"),
        ("jackets", "Jackets"),
        ("trousers", "Trousers"),
        ("footwear", "Footwear"),
        ("golf balls", "Golf Balls"),
        ("hats", "Hats"),
        ("trolley", "Trolleys"),
        ("gps watches", "GPS Watches"),
        ("tees", "Tees"),
        ("gloves", "Gloves"),
    )

    BRAND = (
        ("adidas", "Adidas"),
        ("nike", "Nike"),
        ("srixon", "Srixon"),
        ("taylormade", "Taylormade"),
        ("titleist", "Titleist"),
        ("callaway", "Callaway"),
        ("footjoy", "Footjoy"),
        ("under armour", "Under Armour"),
        ("cobra", "Cobra"),
        ("motocaddy", "Motocaddy"),
        ("ping", "Ping"),
        ("mizuno", "Mizuno"),
        ("garmin", "Garmin"),
        ("calvin klien", "Calvin Klien"),
        ("wilson", "Wilson"),
        ("bushnell", "Bushnell"),
        ("calvin klien", "Calvin Klien"),
    )

    """A model to create and manage reviews"""
    user = models.ForeignKey(
        User, related_name="review_owner", on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=False, blank=False)
    item = models.CharField(
        max_length=50, choices=TYPE_OF_ITEM, default=""
    )
    brand = models.CharField(max_length=50, choices=BRAND, default="")
    product_name=models.CharField(max_length=30, null=False, blank=False)
    description = models.CharField(max_length=2000, null=False, blank=False)
    image = ResizedImageField(
        size=[400, 400], quality=75, upload_to='reviews/', force_format='WEBP',
        blank=False, null=False)
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    posted_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-posted_on"]

    def __str__(self):
        return self.title
