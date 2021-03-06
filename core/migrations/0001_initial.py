# Generated by Django 2.0.6 on 2018-06-12 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Itens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome:')),
                ('slug', models.SlugField(verbose_name='Atalho:')),
                ('cor', models.CharField(blank=True, max_length=20, verbose_name='Cor:')),
                ('image', models.ImageField(upload_to='media', verbose_name='Imagem:')),
            ],
        ),
    ]
