# Generated by Django 4.1.3 on 2022-11-15 16:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=15, null=True)),
                ('last_name', models.CharField(blank=True, max_length=15, null=True)),
                ('phone', models.CharField(blank=True, max_length=13, null=True)),
                ('time_to_call', models.DateTimeField(default=datetime.datetime.now)),
                ('linkedin_url', models.CharField(max_length=100)),
                ('github_url', models.CharField(max_length=100)),
                ('free_text_comments', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Candidate Info',
            },
        ),
    ]
