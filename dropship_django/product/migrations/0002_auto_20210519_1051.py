# Generated by Django 3.2.2 on 2021-05-19 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='specifications',
            field=models.JSONField(blank=True, null=True, verbose_name='Additional Store specifications'),
        ),
        migrations.AlterField(
            model_name='baseproductmodel',
            name='specifications',
            field=models.JSONField(blank=True, null=True, verbose_name='additional product specifications'),
        ),
        migrations.AlterField(
            model_name='childcategory',
            name='specifications',
            field=models.JSONField(blank=True, null=True, verbose_name='Additional Child-category specifications'),
        ),
        migrations.AlterField(
            model_name='parentcategory',
            name='specifications',
            field=models.JSONField(blank=True, null=True, verbose_name='Additional Parent-category specifications'),
        ),
        migrations.AlterField(
            model_name='storedirectory',
            name='specifications',
            field=models.JSONField(blank=True, null=True, verbose_name='Additional Directory specifications'),
        ),
    ]
