# Generated by Django 2.0 on 2017-11-05 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctfSite', '0002_auto_20171105_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='num2',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='team',
            name='qq2',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='team',
            name='st2',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='team',
            name='stnum2',
            field=models.CharField(max_length=50),
        ),
    ]
