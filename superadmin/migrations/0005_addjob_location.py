# Generated by Django 3.2.12 on 2022-03-01 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0004_addjob_prize'),
    ]

    operations = [
        migrations.AddField(
            model_name='addjob',
            name='location',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
