# Generated by Django 4.2.8 on 2024-03-10 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='golfer',
            field=models.CharField(choices=[('barry power', 'Barry Power'), ('brendan mcdaid', 'Brendan McDaid'), ('david mortimer', 'David Mortimer'), ("shane o'grady", "Shane O'Grady"), ('john langan', 'John Langan'), ('hazel kavanagh', 'Hazel Kavanagh'), ('noel fox', 'Noel Fox')], default='', max_length=200),
        ),
    ]
