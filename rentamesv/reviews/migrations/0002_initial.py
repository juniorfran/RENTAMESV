# Generated by Django 4.2.5 on 2023-10-04 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='reviewed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_given', to='users.renter'),
        ),
    ]
