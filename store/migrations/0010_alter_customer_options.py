# Generated by Django 4.1.2 on 2022-11-17 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_product_confectionery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['id'], 'permissions': [('view_history', 'Can view history')]},
        ),
    ]
