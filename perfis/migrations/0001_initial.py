# Generated by Django 2.1.5 on 2019-01-07 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=15)),
                ('nome_empresa', models.CharField(max_length=255)),
            ],
        ),
    ]
