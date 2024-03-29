# Generated by Django 2.2.2 on 2019-07-03 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myknowapp', '0015_auto_20190703_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='depth',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Depth (m)'),
        ),
        migrations.AddField(
            model_name='entity',
            name='frequency',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Frequency (Hz)'),
        ),
        migrations.AddField(
            model_name='entity',
            name='length',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Length (m)'),
        ),
        migrations.AddField(
            model_name='entity',
            name='wavelength',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Wavelength (m)'),
        ),
        migrations.AddField(
            model_name='entity',
            name='width',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Width (m)'),
        ),
    ]
