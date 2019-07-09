# Generated by Django 2.2.2 on 2019-07-01 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myknowapp', '0007_auto_20190701_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entity',
            name='is_composed_of',
        ),
        migrations.AddField(
            model_name='entity',
            name='components',
            field=models.ManyToManyField(blank=True, related_name='compounds', to='myknowapp.Entity'),
        ),
    ]
