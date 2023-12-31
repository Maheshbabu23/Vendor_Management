# Generated by Django 4.2.7 on 2023-12-05 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0005_alter_vendor_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalperformance',
            name='average_response_time',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='historicalperformance',
            name='fulfillment_rate',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='historicalperformance',
            name='on_time_delivery_rate',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='historicalperformance',
            name='quality_rating_avg',
            field=models.FloatField(default=0.0),
        ),
    ]
