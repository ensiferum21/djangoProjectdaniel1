# Generated by Django 4.0.3 on 2022-03-12 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0005_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, default='media/images/SimplifiedRomaniaMap.PNG', upload_to='images/'),
        ),
    ]
