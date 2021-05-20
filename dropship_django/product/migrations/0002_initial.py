# Generated by Django 3.2.2 on 2021-05-19 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='storedirectory',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_directories', to='profile.vendorprofile'),
        ),
        migrations.AddField(
            model_name='storedirectory',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directories', to='product.store'),
        ),
        migrations.AddField(
            model_name='store',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stores', to='profile.vendorprofile'),
        ),
        migrations.AddField(
            model_name='parentcategory',
            name='directory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_categories', to='product.storedirectory'),
        ),
        migrations.AddField(
            model_name='parentcategory',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_categories', to='profile.vendorprofile'),
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.baseproductmodel'),
        ),
        migrations.AddField(
            model_name='childcategory',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_categories', to='profile.vendorprofile'),
        ),
        migrations.AddField(
            model_name='childcategory',
            name='parent',
            field=models.ManyToManyField(related_name='child_categories', to='product.ParentCategory'),
        ),
        migrations.AddField(
            model_name='baseproductmodel',
            name='child_category',
            field=models.ManyToManyField(related_name='child_products', to='product.ChildCategory'),
        ),
        migrations.AddField(
            model_name='baseproductmodel',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='profile.vendorprofile'),
        ),
        migrations.AddField(
            model_name='baseproductmodel',
            name='parent_category',
            field=models.ManyToManyField(related_name='parent_products', to='product.ParentCategory'),
        ),
        migrations.AddField(
            model_name='baseproductmodel',
            name='store',
            field=models.ManyToManyField(related_name='store_products', to='product.Store'),
        ),
    ]
