# Generated by Django 4.1.13 on 2024-03-28 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_remove_cartitem_cart_remove_cartitem_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='paymentinfo',
            name='order',
        ),
        migrations.RemoveField(
            model_name='paymentinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
        migrations.DeleteModel(
            name='PaymentInfo',
        ),
    ]
