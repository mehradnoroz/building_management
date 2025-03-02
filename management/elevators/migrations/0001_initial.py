# Generated by Django 5.1.4 on 2024-12-23 15:23

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('building', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elevators',
            fields=[
                ('e_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('e_is_active', models.BooleanField(default=True)),
                ('e_maintenance_date_services', models.DateField(blank=True, null=True)),
                ('e_manufacturer', models.CharField(blank=True, max_length=100, null=True)),
                ('e_email_manufacturer', models.EmailField(blank=True, max_length=254, null=True)),
                ('e_send_message_with_email', models.BooleanField(default=False)),
                ('e_phone_manufacturer', models.CharField(blank=True, max_length=13, null=True)),
                ('e_send_message_with_sms', models.BooleanField(default=False)),
                ('e_telephone_manufacturer', models.CharField(blank=True, max_length=11, null=True)),
                ('e_text_for_send_with_email_or_sms', models.TextField(blank=True, null=True)),
                ('e_cost_for_services_monthly', models.PositiveIntegerField(default=0)),
                ('e_building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='elevatorss', to='building.building')),
            ],
        ),
    ]
