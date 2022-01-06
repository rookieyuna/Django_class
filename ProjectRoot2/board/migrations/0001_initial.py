# Generated by Django 4.0 on 2022-01-06 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titles', models.CharField(max_length=50)),
                ('contents', models.TextField()),
                ('mainphoto', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
