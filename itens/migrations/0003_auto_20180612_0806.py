# Generated by Django 2.0.6 on 2018-06-12 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itens', '0002_auto_20180612_0739'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itens',
            options={'ordering': ['name'], 'verbose_name': 'Itens'},
        ),
    ]
