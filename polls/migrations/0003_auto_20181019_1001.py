# Generated by Django 2.1.1 on 2018-10-19 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20181015_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.BooleanField(default=True, verbose_name='状态'),
        ),
    ]
