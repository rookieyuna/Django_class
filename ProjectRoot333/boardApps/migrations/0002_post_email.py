# Generated by Django 4.0 on 2022-01-06 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardApps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
