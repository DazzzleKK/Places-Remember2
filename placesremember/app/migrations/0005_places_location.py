# Generated by Django 4.1.3 on 2022-12-01 04:24

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_alter_places_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="places",
            name="location",
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]
