# Generated by Django 4.2.5 on 2023-10-04 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('vehicles', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('paymentmethod', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicleowner',
            name='rented_vehicles',
            field=models.ManyToManyField(blank=True, related_name='owners', to='vehicles.vehicle'),
        ),
        migrations.AddField(
            model_name='vehicleowner',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_owner_profile', to='users.user'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='users.user'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='custom_users', related_query_name='custom_user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='custom_users_permissions', related_query_name='custom_user_permission', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='users.renter'),
        ),
        migrations.AddField(
            model_name='renter',
            name='bookings',
            field=models.ManyToManyField(blank=True, related_name='renters', to='vehicles.booking'),
        ),
        migrations.AddField(
            model_name='renter',
            name='preferred_payment_methods',
            field=models.ManyToManyField(related_name='preferred_pago_renters', to='paymentmethod.paymentmethod'),
        ),
        migrations.AddField(
            model_name='renter',
            name='preferred_vehicle_types',
            field=models.ManyToManyField(related_name='preferred_renters', to='vehicles.vehicletype'),
        ),
        migrations.AddField(
            model_name='renter',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='renter_profile', to='users.user'),
        ),
    ]
