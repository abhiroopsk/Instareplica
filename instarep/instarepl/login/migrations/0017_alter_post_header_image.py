# Generated by Django 4.1.3 on 2022-12-03 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_delete_displayusername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
