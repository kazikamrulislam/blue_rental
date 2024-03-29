# Generated by Django 5.0.3 on 2024-03-24 18:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_move_in_cost_listing_for_sale_listing_map_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='listing',
            name='for_sale',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='is_available',
        ),
        migrations.AddField(
            model_name='listing',
            name='property_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='listings.property_status'),
        ),
    ]
