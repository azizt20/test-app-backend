# Generated by Django 4.1.4 on 2022-12-07 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testa', '0003_alter_optionmodel_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='PINFL',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]