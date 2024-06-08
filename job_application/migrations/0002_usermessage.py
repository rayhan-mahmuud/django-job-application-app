# Generated by Django 5.0.6 on 2024-06-08 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=250)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]