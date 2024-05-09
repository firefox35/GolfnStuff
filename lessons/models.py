from django.db import models


# Create your models here.
class Lessons(models.Model):

    PRO = (
        ("barry power", "Barry Power"),
        ("brendan mcdaid", "Brendan McDaid"),
        ("david mortimer", "David Mortimer"),
        ("shane o'grady", "Shane O'Grady"),
        ("hazel kavanagh", "Hazel Kavanagh"),
        ("john langan", "John Langan"),
        ("noel fox", "Noel Fox"),
    )

    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=40)
    phone = models.IntegerField()
    golfer = models.CharField(max_length=50, choices=PRO,
                              default="Barry Power")
    date = models.DateTimeField(null=False, blank=True)
    comment = models.TextField(max_length=2000, null=False, blank=False)

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lesson"

    def __str__(self):
        return self.name
