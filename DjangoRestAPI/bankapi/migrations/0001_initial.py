# Generated by Django 2.2.3 on 2019-07-14 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigIntegerField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('ifsc', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('branch', models.CharField(max_length=74, null=True)),
                ('address', models.CharField(max_length=195, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('district', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=26, null=True)),
                ('bank_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapi.Bank')),
            ],
        ),
    ]
