# Generated by Django 4.2.7 on 2025-06-27 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('location', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='event_images/')),
                ('registration_url', models.URLField(blank=True, null=True)),
            ],
            options={
                'ordering': ['start_date'],
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('important', models.BooleanField(default=False)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='notice_attachments/')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
