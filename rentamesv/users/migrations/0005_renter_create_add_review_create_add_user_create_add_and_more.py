# Generated by Django 4.2.5 on 2023-10-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_userprofile_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='renter',
            name='create_add',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='create_add',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='create_add',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='create_add',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='vehicleowner',
            name='create_add',
            field=models.DateField(null=True),
        ),
    ]
