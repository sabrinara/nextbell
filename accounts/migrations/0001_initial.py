# Generated by Django 5.0.2 on 2024-11-06 14:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='accounts/media/profile_pics/')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('division', models.CharField(blank=True, choices=[('Dhaka', 'Dhaka'), ('Chittagong', 'Chittagong'), ('Khulna', 'Khulna'), ('Sylhet', 'Sylhet'), ('Rajshahi', 'Rajshahi'), ('Barishal', 'Barishal'), ('Rangpur', 'Rangpur'), ('Mymensingh', 'Mymensingh')], max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='AbstractUserDetails', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]