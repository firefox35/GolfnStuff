# Generated by Django 3.2.24 on 2024-02-25 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='clothing_size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'X Large'), ('2XL', 'XX Large')], default='S', max_length=3),
        ),
        migrations.AddField(
            model_name='product',
            name='degree',
            field=models.CharField(choices=[('46', 'Forty Six'), ('48', 'Forty Eight'), ('50', 'Fifty'), ('52', 'Fifty Two'), ('54', 'Fifty Four'), ('56', 'Fifty Six'), ('58', 'Fifty Eight'), ('60', 'Sixty'), ('64', 'Sixty Four')], default='46', max_length=2),
        ),
        migrations.AddField(
            model_name='product',
            name='shaft',
            field=models.CharField(choices=[('regular', 'Regular'), ('stiff', 'Stiff'), ('senior', 'Senior')], default='Regular', max_length=7),
        ),
        migrations.AddField(
            model_name='product',
            name='shoe_size',
            field=models.CharField(choices=[('3', 'Three'), ('4', 'Four'), ('5', 'Five'), ('6', 'Six'), ('7', 'Seven'), ('8', 'Eight'), ('9', 'Nine'), ('10', 'Ten'), ('11', 'Eleven'), ('12', 'Twelve'), ('13', 'Thirteen')], default='3', max_length=2),
        ),
    ]
