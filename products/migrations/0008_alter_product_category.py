# Generated by Django 4.0 on 2024-01-27 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_category_fit_style_texture_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=False, null=False, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category'),
        ), # 여기 수정해야할 수도 있음
    ]
