# Generated by Django 3.2.13 on 2022-09-27 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIHUB', '0004_auto_20220926_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='accountType',
            field=models.CharField(choices=[('student', 'Student'), ('admin', 'Admin'), ('PI', 'PI'), ('client_admin', 'Client_Admin'), ('client_team', 'Client_Team')], default='student', max_length=25),
        ),
    ]
