# Generated by Django 4.2 on 2023-04-12 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0008_band_like_new"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="band",
            name="like_new",
        ),
    ]
