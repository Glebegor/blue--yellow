# Generated by Django 4.0.6 on 2022-08-05 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_rename_goodsmodel_goodesmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodesmodel',
            name='img',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
