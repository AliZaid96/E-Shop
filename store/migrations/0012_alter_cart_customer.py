# Generated by Django 4.0 on 2022-10-19 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0005_remove_address_customer_address_user'),
        ('store', '0011_cart_subtotal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_accounts.customer'),
        ),
    ]
