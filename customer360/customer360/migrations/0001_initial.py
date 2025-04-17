# Generated by Django 3.1.3 on 2025-04-17 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.CharField(choices=[('phone', 'Phone'), ('sms', 'SMS'), ('email', 'Email'), ('letter', 'Letter')], max_length=15)),
                ('direction', models.CharField(choices=[('inbound', 'Inbound'), ('outbound', 'Outbound')], max_length=10)),
                ('interaction_date', models.DateField(auto_now_add=True)),
                ('summary', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer360.customer')),
            ],
        ),
    ]
