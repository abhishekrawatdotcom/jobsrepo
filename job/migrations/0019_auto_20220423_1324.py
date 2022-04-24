# Generated by Django 3.2.12 on 2022-04-23 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0018_user_middlename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='SSOkey',
            new_name='caddress1',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Criteria',
            new_name='cnationlity',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='graduationbu',
            new_name='ctehsil',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='graduationmo',
            new_name='domicial',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='graduationpgc',
            new_name='domicial_certificate',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='graduationpy',
            new_name='domicial_date',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='graduationsc',
            new_name='domicial_district',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='graduationtm',
            new_name='graduationcollege',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='postgraduationbu',
            new_name='graduationdate',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='postgraduationmo',
            new_name='graduationgrade',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='postgraduationpgc',
            new_name='graduationobtainmarks',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='postgraduationpy',
            new_name='graduationtotalmarks',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='postgraduationsc',
            new_name='graduationuniversity',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='postgraduationtm',
            new_name='hsccollege',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='tenthbu',
            new_name='hscdate',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='tenthmo',
            new_name='hscgrade',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='tenthpgc',
            new_name='hscobtainmarks',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='tenthpy',
            new_name='hsctotalmarks',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='tenthsc',
            new_name='hscuniversity',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='tenthtm',
            new_name='phdcollege',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='twelvebu',
            new_name='phddate',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='twelvemo',
            new_name='phdgrade',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='twelvepgc',
            new_name='phdobtainmarks',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='twelvepy',
            new_name='phdtotalmarks',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='twelvesc',
            new_name='phduniversity',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='twelvetm',
            new_name='postgraduationcollege',
        ),
        migrations.RemoveField(
            model_name='user',
            name='aadhar',
        ),
        migrations.AddField(
            model_name='user',
            name='caddress2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='ccity',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='cdistrict',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='clandmark',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='cpin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='cstate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='expectedsalary',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='graduationdoc',
            field=models.ImageField(blank=True, null=True, upload_to='graduationdoc'),
        ),
        migrations.AddField(
            model_name='user',
            name='hscdoc',
            field=models.ImageField(blank=True, null=True, upload_to='hscdoc'),
        ),
        migrations.AddField(
            model_name='user',
            name='identity_desc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='identity_detail',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='landmark',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='moreappointmen',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='morecompanyname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='moredepartment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='moredesignation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='moreexpectedsalary',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='moremonth',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='moresalary',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='moreyear',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phddoc',
            field=models.ImageField(blank=True, null=True, upload_to='phddoc'),
        ),
        migrations.AddField(
            model_name='user',
            name='postgraduationdate',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='postgraduationdoc',
            field=models.ImageField(blank=True, null=True, upload_to='postgraduationdoc'),
        ),
        migrations.AddField(
            model_name='user',
            name='postgraduationgrade',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='postgraduationobtainmarks',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='postgraduationtotalmarks',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='postgraduationuniversity',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='qualification',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='salary',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='ssccollege',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='sscdate',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='sscdoc',
            field=models.ImageField(blank=True, null=True, upload_to='sscdoc'),
        ),
        migrations.AddField(
            model_name='user',
            name='sscgrade',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='sscobtainmarks',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='ssctotalmarks',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='sscuniversity',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
