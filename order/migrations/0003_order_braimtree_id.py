# Generated by Django 3.0.6 on 2020-10-08 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20200929_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='braimtree_id',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
