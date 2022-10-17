# Generated by Django 4.0.4 on 2022-06-03 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0003_alter_studentcourseclassroom_course_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.courseclassroom', to_field='course_id'),
        ),
    ]
