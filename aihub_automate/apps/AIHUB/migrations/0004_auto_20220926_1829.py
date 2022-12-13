# Generated by Django 3.2.13 on 2022-09-26 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIHUB', '0003_companycash'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecttitle',
            name='projectTitle',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='projecttitle',
            name='question1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projecttitle',
            name='question2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projecttitle',
            name='noveltyProject',
            field=models.TextField(blank=True, null=True),
        ),
    ]