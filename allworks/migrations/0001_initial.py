# Generated by Django 4.2.2 on 2023-06-11 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('focus', 'Focus'), ('team', 'Team'), ('conference', 'Conference')], default='team', max_length=20)),
                ('capacity', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='allworks.resident')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='allworks.room')),
            ],
        ),
    ]
