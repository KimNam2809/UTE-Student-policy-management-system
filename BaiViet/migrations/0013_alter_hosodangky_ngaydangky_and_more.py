# Generated by Django 4.2.13 on 2024-06-03 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaiViet', '0012_sinhvien_image_alter_sinhvien_gioitinh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hosodangky',
            name='Ngaydangky',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='hosodangky',
            name='Ngayxacnhan',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
