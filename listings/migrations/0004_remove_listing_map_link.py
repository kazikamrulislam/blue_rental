# Generated by Django 5.0.3 on 2024-03-24 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_property_status_remove_listing_for_sale_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='map_link',
        ),
    ]
