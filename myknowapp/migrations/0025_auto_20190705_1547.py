# Generated by Django 2.2.2 on 2019-07-05 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myknowapp', '0024_auto_20190705_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='speed_rotation',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Rotation speed (km/h)'),
        ),
    ]
