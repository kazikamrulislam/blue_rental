# Generated by Django 5.0.3 on 2024-03-25 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_listing_status_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='status_color',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
