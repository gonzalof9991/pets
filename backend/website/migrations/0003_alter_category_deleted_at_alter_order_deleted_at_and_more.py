# Generated by Django 5.0.7 on 2024-07-15 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_product_image_url_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='deleted_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='deleted_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='deleted_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='deleted_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]