# Generated by Django 4.0.4 on 2022-05-21 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0002_alter_assignment_course_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcourseclassroom',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.courseclassroom', to_field='course_id'),
        ),
    ]
