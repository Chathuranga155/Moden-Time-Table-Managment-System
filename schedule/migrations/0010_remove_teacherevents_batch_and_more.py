# Generated by Django 5.1.2 on 2024-10-13 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0009_batch_degree_teacherevents'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherevents',
            name='batch',
        ),
        migrations.RemoveField(
            model_name='teacherevents',
            name='degree',
        ),
        migrations.DeleteModel(
            name='Batch',
        ),
        migrations.DeleteModel(
            name='Degree',
        ),
        migrations.DeleteModel(
            name='TeacherEvents',
        ),
    ]