# Generated by Django 4.2.8 on 2024-03-21 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0006_alter_lessons_comment_alter_lessons_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='date',
            field=models.DateField(),
        ),
    ]
