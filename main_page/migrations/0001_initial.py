# Generated by Django 5.2.3 on 2025-06-25 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, null=True)),
                ('technology', models.CharField(blank=True, null=True)),
                ('image_url', models.URLField()),
                ('project_link', models.URLField(blank=True, null=True)),
                ('project_tecnology', models.ManyToManyField(blank=True, to='main_page.technology')),
            ],
        ),
    ]
