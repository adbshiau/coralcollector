# Generated by Django 4.0.4 on 2022-04-27 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_name', models.CharField(max_length=100)),
                ('scientific_name', models.CharField(max_length=100)),
                ('coral_type', models.CharField(choices=[('S', 'Soft'), ('L', 'Large Polyp Stony'), ('P', 'Small Polyp Stony'), ('A', 'Anemone')], default='S', max_length=10)),
                ('difficulty', models.CharField(choices=[('V', 'Very Sensitive'), ('S', 'Sensitive'), ('M', 'Moderate'), ('H', 'Hardy'), ('A', 'Very Hardy')], default='M', max_length=10)),
                ('lighting', models.CharField(choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High'), ('V', 'Very High')], default='M', max_length=10)),
                ('water_flow', models.CharField(choices=[('L', 'Low'), ('M', 'Moderate'), ('S', 'Strong')], default='M', max_length=10)),
                ('notes', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('temp', models.DecimalField(decimal_places=2, max_digits=5)),
                ('kh', models.DecimalField(decimal_places=1, max_digits=3)),
                ('po4', models.DecimalField(decimal_places=1, max_digits=3)),
                ('no3', models.IntegerField()),
                ('coral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.coral')),
            ],
        ),
    ]
