# Generated by Django 4.2.8 on 2024-03-10 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_remove_review_brand_remove_review_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='image',
        ),
        migrations.AddField(
            model_name='review',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
