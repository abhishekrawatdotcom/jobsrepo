# Generated by Django 3.2.12 on 2022-02-12 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_auto_20220212_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='economically',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
