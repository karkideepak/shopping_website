# Generated by Django 4.1.1 on 2022-10-02 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_alter_customer_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default=1, upload_to='product_images'),
            preserve_default=False,
        ),
    ]
