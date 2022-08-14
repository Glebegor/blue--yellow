# Generated by Django 4.0.6 on 2022-08-04 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_delete_goodsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='goodsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('version', models.CharField(max_length=255)),
                ('article', models.CharField(max_length=255)),
                ('material', models.CharField(max_length=255)),
                ('furniture', models.CharField(max_length=255)),
                ('colors', models.CharField(max_length=255)),
                ('price', models.IntegerField(max_length=255)),
            ],
        ),
    ]