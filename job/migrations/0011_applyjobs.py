# Generated by Django 3.2.12 on 2022-02-18 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_user_criteria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applyjobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usr', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
