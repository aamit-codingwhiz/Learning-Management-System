# Generated by Django 4.0.4 on 2022-06-07 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0007_alter_assignment_file_path'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='file_path',
            new_name='uploaded_file',
        ),
    ]