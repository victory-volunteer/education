# Generated by Django 2.2 on 2020-09-05 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200905_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('female', '女'), ('male', '男')], max_length=6, verbose_name='性别'),
        ),
    ]
