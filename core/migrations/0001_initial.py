# Generated by Django 3.0.1 on 2020-01-03 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SlideShowPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=None, upload_to='slide show pics')),
                ('description', models.CharField(max_length=300)),
                ('slideshow', models.URLField()),
            ],
        ),
    ]