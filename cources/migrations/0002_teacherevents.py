# Generated by Django 5.1.2 on 2024-10-13 09:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('color', models.CharField(max_length=7)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cources.batch')),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cources.degree')),
            ],
        ),
    ]
