# Generated by Django 3.0.5 on 2020-04-19 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0008_auto_20200419_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='counties',
            name='cc_4',
        ),
        migrations.RemoveField(
            model_name='counties',
            name='engtype_4',
        ),
        migrations.RemoveField(
            model_name='counties',
            name='gid_3',
        ),
        migrations.RemoveField(
            model_name='counties',
            name='gid_4',
        ),
        migrations.RemoveField(
            model_name='counties',
            name='name_3',
        ),
        migrations.RemoveField(
            model_name='counties',
            name='name_4',
        ),
        migrations.RemoveField(
            model_name='counties',
            name='type_4',
        ),
        migrations.RemoveField(
            model_name='counties',
            name='varname_4',
        ),
        migrations.AddField(
            model_name='counties',
            name='cc_2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='counties',
            name='engtype_2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='counties',
            name='hasc_2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='counties',
            name='nl_name_1',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='counties',
            name='nl_name_2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='counties',
            name='type_2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='counties',
            name='varname_2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
