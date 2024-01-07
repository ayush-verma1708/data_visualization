# Generated by Django 4.2.9 on 2024-01-07 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intensity', models.FloatField()),
                ('Likelihood', models.FloatField()),
                ('Relevance', models.FloatField()),
                ('Year', models.CharField(max_length=255)),
                ('Country', models.CharField(max_length=255)),
                ('Topics', models.CharField(max_length=255)),
                ('Region', models.CharField(max_length=255)),
                ('City', models.CharField(max_length=255)),
            ],
        ),
    ]
