# Generated by Django 3.0.1 on 2020-02-05 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('content', models.TextField(blank=True, max_length=5000, null=True)),
                ('date', models.DateTimeField()),
                ('pic1', models.ImageField(blank=True, default=None, null=True, upload_to='event pics')),
                ('pic2', models.ImageField(blank=True, default=None, null=True, upload_to='event pics')),
                ('pic3', models.ImageField(blank=True, default=None, null=True, upload_to='event pics')),
                ('pic4', models.ImageField(blank=True, default=None, null=True, upload_to='event pics')),
                ('pic5', models.ImageField(blank=True, default=None, null=True, upload_to='event pics')),
                ('pic6', models.ImageField(blank=True, default=None, null=True, upload_to='event pics')),
                ('pic7', models.ImageField(blank=True, default=None, null=True, upload_to='event pics')),
                ('pic8', models.ImageField(blank=True, default=None, null=True, upload_to='event pics')),
                ('pic9', models.ImageField(blank=True, default=None, null=True, upload_to='event pics')),
                ('pic10', models.ImageField(blank=True, default=None, null=True, upload_to='event pics')),
                ('pic11', models.ImageField(blank=True, default=None, null=True, upload_to='event pics')),
                ('status', models.CharField(choices=[('True', 'Upcoming'), ('False', 'Happened')], default=True, max_length=10)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('attended', models.CharField(choices=[('A', 'Attended'), ('NA', 'Not Attended')], default='NA', max_length=10)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='registrations')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
