# Generated by Django 3.2.3 on 2021-05-28 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_alter_productimage_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='my_app'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='my_app'),
        ),
    ]
