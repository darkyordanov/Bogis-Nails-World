# Generated by Django 5.0.1 on 2024-02-12 07:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_remove_naildesign_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('Dark', 'Dark'), ('Light', 'Light'), ('Red', 'Red'), ('Pink', 'Pink'), ('Blue', 'Blue'), ('Purple', 'Purple'), ('White', 'White'), ('Black', 'Black'), ('Gold', 'Gold'), ('Nude', 'Nude'), ('Yellow', 'Yellow'), ('Orange', 'Orange'), ('Green', 'Green'), ('Brown', 'Brown'), ('Gray', 'Gray')], max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='naildesign',
            old_name='modifited_at',
            new_name='modified_at',
        ),
        migrations.RemoveField(
            model_name='naildesign',
            name='color',
        ),
        migrations.AlterField(
            model_name='naildesign',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='naildesign',
            name='colors',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.color'),
            preserve_default=False,
        ),
    ]
