# Generated by Django 4.1.13 on 2024-03-28 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_rename_sold_product_discount_remove_orderitem_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
