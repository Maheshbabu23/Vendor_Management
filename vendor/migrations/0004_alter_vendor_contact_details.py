# Generated by Django 4.2.7 on 2023-12-04 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_alter_vendor_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='contact_details',
            field=models.TextField(),
        ),
    ]
