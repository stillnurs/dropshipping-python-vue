# Generated by Django 3.2.2 on 2021-05-11 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
