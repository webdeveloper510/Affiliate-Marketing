# Generated by Django 4.1.7 on 2023-05-03 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CampaignApp', '0019_notification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='vendor_id',
            new_name='vendor',
        ),
    ]
