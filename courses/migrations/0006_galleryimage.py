# Generated by Django 4.2.7 on 2025-07-01 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0005_download_executivemessage_teacherstaff"),
    ]

    operations = [
        migrations.CreateModel(
            name="GalleryImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="gallery_images/")),
                ("title", models.CharField(blank=True, max_length=200)),
                ("description", models.TextField(blank=True)),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
