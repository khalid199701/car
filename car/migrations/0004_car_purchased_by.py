# Generated by Django 4.2.7 on 2024-01-13 17:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='purchased_by',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]