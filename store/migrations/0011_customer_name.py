# Generated by Django 4.1.2 on 2022-11-17 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_customer_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(default='ali', max_length=85),
            preserve_default=False,
        ),
    ]
