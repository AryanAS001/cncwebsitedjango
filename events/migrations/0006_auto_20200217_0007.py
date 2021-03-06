# Generated by Django 3.0.1 on 2020-02-16 18:37

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_certi_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='certi_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
