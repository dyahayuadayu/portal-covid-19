# Generated by Django 3.0.5 on 2020-04-19 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0005_auto_20200419_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counties',
            name='dis',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
