# Generated by Django 4.0.6 on 2022-08-08 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_alter_goodesmodel_imagegoodes'),
    ]

    operations = [
        migrations.CreateModel(
            name='ordersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('brand', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]
