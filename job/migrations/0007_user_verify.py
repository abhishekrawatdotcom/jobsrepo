# Generated by Django 3.2.12 on 2022-02-15 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_user_economically'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verify',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
