# Generated by Django 4.2.6 on 2023-11-03 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_studentdetails_admin_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetails',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
