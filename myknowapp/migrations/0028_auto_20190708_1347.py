# Generated by Django 2.2.2 on 2019-07-08 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myknowapp', '0027_auto_20190708_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entity',
            old_name='perimeter',
            new_name='a_perimeter',
        ),
        migrations.RenameField(
            model_name='entity',
            old_name='speed',
            new_name='a_speed',
        ),
        migrations.RenameField(
            model_name='entity',
            old_name='speed_rotation',
            new_name='a_speed_rotation',
        ),
    ]
