# Generated by Django 3.0.2 on 2020-02-21 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeLoader', '0003_auto_20200221_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photos/'),
        ),
    ]
