# Generated by Django 3.0.4 on 2020-04-04 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import exams.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='file',
            field=models.FileField(null=True, upload_to=exams.models.Report.get_upload_handler),
        ),
        migrations.AddField(
            model_name='report',
            name='medico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='report',
            name='diagnostic',
            field=models.CharField(max_length=100),
        ),
    ]
