# Generated by Django 3.0.4 on 2020-04-12 22:46

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=accounts.models.Medico.get_upload_handler),
        ),
    ]
