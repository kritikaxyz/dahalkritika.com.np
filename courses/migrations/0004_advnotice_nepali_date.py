# Generated by Django 4.2.7 on 2025-07-01 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0003_advnotice"),
    ]

    operations = [
        migrations.AddField(
            model_name="advnotice",
            name="nepali_date",
            field=models.CharField(
                blank=True,
                help_text="Date in Nepali calendar (e.g., 2081-03-15)",
                max_length=20,
            ),
        ),
    ]
