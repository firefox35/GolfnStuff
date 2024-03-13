from django.contrib import admin
from .models import Lessons
# Register your models here.

class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'golfer',
        'date',
        'time',
    )


admin.site.register(Lessons, LessonAdmin)