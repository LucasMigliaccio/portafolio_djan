# Generated by Django 4.0.3 on 2022-08-16 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_lenguajes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=25)),
                ('image', models.ImageField(upload_to='lenguajes/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Databases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=25)),
                ('image', models.ImageField(upload_to='lenguajes/images/')),
            ],
        ),
    ]
