# Generated by Django 5.0.6 on 2024-05-27 14:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaiViet', '0009_alter_chitiethoso_mtc'),
    ]

    operations = [
        migrations.AddField(
            model_name='hosodangky',
            name='MDT',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hosodangky', to='BaiViet.doituongchinhsach'),
        ),
        migrations.AlterField(
            model_name='quydinhapdung',
            name='MDT',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BaiViet.doituongchinhsach'),
        ),
    ]
