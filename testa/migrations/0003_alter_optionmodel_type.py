# Generated by Django 4.1.4 on 2022-12-07 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testa', '0002_optionmodel_testmodel_resultmodel_questionmodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optionmodel',
            name='type',
            field=models.SmallIntegerField(choices=[(1, 'simple'), (2, 'text'), (3, 'many choose')], db_index=True, default=1),
        ),
    ]
