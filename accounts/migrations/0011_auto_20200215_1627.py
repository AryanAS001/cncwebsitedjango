# Generated by Django 3.0.1 on 2020-02-15 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200205_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='branch',
            field=models.CharField(choices=[('CE', 'CE'), ('IT', 'IT'), ('ECE', 'ECE'), ('ECS', 'ECS'), ('EIC', 'EIC'), ('EL', 'EL'), ('MECH', 'MECH'), ('CIVIL', 'CIVIL'), ('Mathematics', 'Mathematics'), ('Chemistry', 'Chemistry'), ('Physics', 'Physics')], max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='course',
            field=models.CharField(choices=[('BTECH', 'Btech'), ('MTECH', 'Mtech'), ('BCA', 'BCA'), ('MCA', 'MCA'), ('BSC', 'Bsc'), ('MSC', 'Msc'), ('MBA', 'MBA')], max_length=50),
        ),
    ]
