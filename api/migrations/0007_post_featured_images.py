# Generated by Django 2.1.7 on 2019-03-21 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_post_featured_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_images',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]
