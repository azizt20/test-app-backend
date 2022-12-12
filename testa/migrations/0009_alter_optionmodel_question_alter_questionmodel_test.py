# Generated by Django 4.1.4 on 2022-12-11 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testa', '0008_remove_optionmodel_point_remove_optionmodel_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optionmodel',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='options', to='testa.questionmodel'),
        ),
        migrations.AlterField(
            model_name='questionmodel',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='testa.testmodel'),
        ),
    ]