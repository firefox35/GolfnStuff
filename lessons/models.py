from django.db import models

# Create your models here.
class Lessons(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()
    golfer = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    comment = models.TextField()

    
    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lesson"

    def __str__(self):
        return self.name



