# Generated by Django 4.1.4 on 2022-12-07 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testa', '0004_alter_usermodel_pinfl_alter_usermodel_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='optionmodel',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='testa.questionmodel'),
        ),
        migrations.AlterField(
            model_name='resultmodel',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='testa.testmodel'),
        ),
    ]
