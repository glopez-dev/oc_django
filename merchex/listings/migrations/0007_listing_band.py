# Generated by Django 4.2 on 2023-04-12 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0006_alter_band_genre"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="band",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="listings.band",
            ),
        ),
    ]
