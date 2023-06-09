# Generated by Django 4.1.7 on 2023-06-21 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CampaignApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='transferdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transferid', models.CharField(blank=True, max_length=200, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('destination', models.CharField(blank=True, max_length=255, null=True)),
                ('influencer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CampaignApp.modashinfluencer')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
