# Generated by Django 4.2.8 on 2024-03-10 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_remove_review_image_review_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='image_url',
        ),
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
