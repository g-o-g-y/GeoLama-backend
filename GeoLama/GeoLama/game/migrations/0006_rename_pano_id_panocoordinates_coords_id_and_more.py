# Generated by Django 4.0.2 on 2022-02-13 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_panocoordinates'),
    ]

    operations = [
        migrations.RenameField(
            model_name='panocoordinates',
            old_name='pano_id',
            new_name='coords_id',
        ),
        migrations.RenameField(
            model_name='panocoordinates',
            old_name='pano_latitude',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='panocoordinates',
            old_name='pano_longitude',
            new_name='longitude',
        ),
    ]
