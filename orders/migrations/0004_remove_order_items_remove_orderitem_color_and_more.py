# Generated by Django 4.1.13 on 2024-04-06 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_remove_product_category_subcategory_and_more'),
        ('orders', '0003_order_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='color',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='size',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product_variant',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.productvariant'),
        ),
    ]
