# Generated by Django 5.1.6 on 2025-02-23 11:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bayesian_networks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='bayesian_network',
        ),
        migrations.AddField(
            model_name='challenge',
            name='name',
            field=models.CharField(default='Challenge', max_length=100),
        ),
        migrations.CreateModel(
            name='BayesianNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network', models.CharField(max_length=255, verbose_name='Bayesian network')),
                ('Challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bayesian_networks', to='bayesian_networks.challenge')),
            ],
        ),
    ]
