# Generated by Django 3.2.12 on 2022-02-17 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_auto_20220216_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Criteria',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
