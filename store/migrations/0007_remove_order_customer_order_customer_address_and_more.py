# Generated by Django 4.0 on 2022-10-19 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_cart_session_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.AddField(
            model_name='order',
            name='customer_address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='customer_email',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='customer_gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='customer_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='delivered_at',
            field=models.DateTimeField(auto_now_add=True, default="2222-10-10"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.FloatField(default=0),
        ),
    ]
