# Generated by Django 2.0.6 on 2018-11-16 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itens', '0003_auto_20181113_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itens',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='itens.Categoria'),
        ),
    ]