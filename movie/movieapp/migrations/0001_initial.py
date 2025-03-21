# Generated by Django 5.1.7 on 2025-03-21 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Movie Title', max_length=255)),
                ('director', models.CharField(help_text='Director Name', max_length=100)),
                ('release_date', models.DateField(help_text='Release Date')),
                ('genre', models.CharField(help_text='Movie Genre', max_length=50)),
                ('rating', models.DecimalField(decimal_places=1, help_text='Movie Rating (e.g., 8.5)', max_digits=3)),
                ('duration', models.IntegerField(help_text='Duration in Minutes')),
            ],
        ),
    ]
