# Generated by Django 2.2 on 2020-08-18 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200818_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('female', '女'), ('male', '男')], max_length=6, verbose_name='性别'),
        ),
    ]
