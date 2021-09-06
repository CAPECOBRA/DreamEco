# Generated by Django 3.1 on 2021-09-01 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0006_auto_20210901_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('PAYMENT INITIATED', 'PAYMENT INITIATED'), ('PAYMENT DONE', 'PAYMENT_DONE'), ('PAYMENT PENDING', 'PAYMENT PENDING')], max_length=50),
        ),
    ]
