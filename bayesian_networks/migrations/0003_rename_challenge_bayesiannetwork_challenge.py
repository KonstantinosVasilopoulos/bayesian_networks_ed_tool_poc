# Generated by Django 5.1.6 on 2025-02-23 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bayesian_networks', '0002_remove_challenge_bayesian_network_challenge_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bayesiannetwork',
            old_name='Challenge',
            new_name='challenge',
        ),
    ]
