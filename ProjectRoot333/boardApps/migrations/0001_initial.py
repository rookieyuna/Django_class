# Generated by Django 4.0 on 2022-01-06 07:59

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
                ('user_name', models.CharField(max_length=5)),
                ('viewCount', models.CharField(default=0, max_length=5)),
                ('postdate', models.DateField(blank=True, null=True)),
                ('titles', models.CharField(max_length=50)),
                ('contents', models.TextField()),
                ('mainphoto', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
