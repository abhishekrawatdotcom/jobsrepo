# Generated by Django 3.2.12 on 2022-02-18 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0014_auto_20220218_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyjobs',
            name='verify',
            field=models.BooleanField(default=False),
        ),
    ]
