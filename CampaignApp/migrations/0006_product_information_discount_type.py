# Generated by Django 4.1.7 on 2023-06-27 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CampaignApp', '0005_modashinfluencer_admin_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_information',
            name='discount_type',
            field=models.TextField(blank=True),
        ),
    ]
