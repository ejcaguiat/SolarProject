# Generated by Django 2.0.5 on 2018-06-20 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SolarDB', '0021_salesproperty_paidstatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaseproperty',
            name='leaseamountperyear',
        ),
        migrations.AddField(
            model_name='leaseproperty',
            name='leaseamountperyear10',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='leaseproperty',
            name='leaseamountperyear15',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='leaseproperty',
            name='leaseamountperyear20',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='leaseproperty',
            name='leaseamountperyear25',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='leaseproperty',
            name='leaseamountperyear30',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='leaseproperty',
            name='leaseamountperyear5',
            field=models.FloatField(default=0),
        ),
    ]