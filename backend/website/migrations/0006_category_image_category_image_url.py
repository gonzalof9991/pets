# Generated by Django 5.0.7 on 2024-07-16 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_product_qualification'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='category',
            name='image_url',
            field=models.URLField(blank=True, default=None, null=True),
        ),
    ]
