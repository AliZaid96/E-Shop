# Generated by Django 4.0 on 2022-10-19 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_cart_session_id_alter_orderitem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='subTotal',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
