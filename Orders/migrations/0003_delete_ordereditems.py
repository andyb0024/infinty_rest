# Generated by Django 3.2.4 on 2021-09-02 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0002_auto_20210829_0525'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderedItems',
        ),
    ]
