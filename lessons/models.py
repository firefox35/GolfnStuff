from django.db import models

# Create your models here.
class Lessons(models.Model):
    GOLFERS = (
        ("barry power","Barry Power"),
        ("brendan mcdaid","Brendan McDaid"),
        ("david mortimer","David Mortimer"),
        ("shane o'grady","Shane O'Grady"),
        ("john langan","John Langan"),
        ("hazel kavanagh","Hazel Kavanagh"),
        ("noel fox","Noel Fox"),
    )

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()
    golfer = models.CharField(max_length=200, choices=GOLFERS, default="")
    date = models.DateField()
    time = models.TimeField()
    comment = models.TextField()

    def __str__(self):
        return self.name


