# Generated by Django 4.0.2 on 2022-02-14 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_rename_pano_id_panocoordinates_coords_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Raining',
        ),
    ]
