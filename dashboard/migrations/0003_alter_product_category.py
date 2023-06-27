# Generated by Django 4.2.1 on 2023-06-26 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_product_category_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Stationary', 'Stationary'), ('Vegetables', 'Vegetables'), ('Drinks', 'Drinks'), ('Fruits', 'Fruits'), ('Cereals', 'Cereals')], max_length=100),
        ),
    ]
