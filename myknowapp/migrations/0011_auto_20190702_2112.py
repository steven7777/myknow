# Generated by Django 2.2.2 on 2019-07-02 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myknowapp', '0010_auto_20190702_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='is_linked_to',
            field=models.ForeignKey(blank=True, help_text="STRONG link (like Earth 'turns around' Sun)", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='linked', to='myknowapp.Entity'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='related',
            field=models.ManyToManyField(blank=True, help_text="WEAK link (like 'is friend of', 'is synonym of', ...)", related_name='_entity_related_+', to='myknowapp.Entity'),
        ),
    ]
