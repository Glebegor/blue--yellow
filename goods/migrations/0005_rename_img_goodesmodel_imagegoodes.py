# Generated by Django 4.0.6 on 2022-08-05 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_alter_goodesmodel_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goodesmodel',
            old_name='img',
            new_name='imageGoodes',
        ),
    ]
