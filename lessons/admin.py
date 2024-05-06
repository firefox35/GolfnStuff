from django.contrib import admin
from .models import Lessons
# Register your models here.

@admin.register(Lessons)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'golfer',
        'date',
    )
