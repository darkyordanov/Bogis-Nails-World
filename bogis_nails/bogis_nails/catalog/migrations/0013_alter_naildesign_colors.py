# Generated by Django 5.0.1 on 2024-02-12 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_alter_naildesign_colors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='naildesign',
            name='colors',
            field=models.CharField(choices=[('Dark', 'Dark'), ('Light', 'Light'), ('Red', 'Red'), ('Pink', 'Pink'), ('Blue', 'Blue'), ('Purple', 'Purple'), ('White', 'White'), ('Black', 'Black'), ('Gold', 'Gold'), ('Nude', 'Nude'), ('Yellow', 'Yellow'), ('Orange', 'Orange'), ('Green', 'Green'), ('Brown', 'Brown'), ('Gray', 'Gray')], max_length=100),
        ),
    ]
