# Generated by Django 4.1.7 on 2023-05-01 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CampaignApp', '0010_campaign_accept'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign_accept',
            name='campaignid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CampaignApp.campaign'),
        ),
    ]
