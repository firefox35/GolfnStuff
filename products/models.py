from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    CLOTHING_SIZES = (
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
        ("Extra Large", "XL"),
        ("XX Large", "2XL"),
    )

    SHOE_SIZES = (
        ("Three","3"),
        ("Four","4"),
        ("Five","5"),
        ("Six","6"),
        ("Seven","7"),
        ("Eight","8"),
        ("Nine","9"),
        ("Ten","10",),
        ("Eleven","11"),
        ("Twelve","12"),
        ("Thirteen","13"),
    )

    SHAFT = (
        ("regular","Regular"),
        ("stiff","Stiff"),
        ("senior","Senior"),
    )

    WEDGE_DEGREE = (
        ("Forty Six","46"),
        ("Forty Eight","48"),
        ("Fifty","50"),
        ("Fifty Two","52"),
        ("Fifty Four","54"),
        ("Fifty Six","56"),
        ("Fifty Eight","58"),
        ("Sixty","60"),
        ("Sixty Four","64"),
    )
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    degree = models.CharField(max_length=11, choices=WEDGE_DEGREE, default="", blank=True,
        null=True)
    shoe_size = models.CharField(max_length=8, choices=SHOE_SIZES, default="", blank=True,
        null=True)
    clothing_size = models.CharField(max_length=11, choices=CLOTHING_SIZES, default="", blank=True,
        null=True)
    shaft = models.CharField(max_length=7, choices=SHAFT, default="Regular", blank=True,
        null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

