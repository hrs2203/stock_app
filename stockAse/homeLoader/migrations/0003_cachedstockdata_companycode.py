# Generated by Django 3.0.2 on 2020-07-18 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeLoader', '0002_cachedstockdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='cachedstockdata',
            name='companyCode',
            field=models.CharField(default='', max_length=50, verbose_name='Code'),
        ),
    ]