# Generated by Django 3.2.7 on 2021-10-02 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0003_auto_20211002_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocery',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='grocery',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='grocery',
            name='warranty',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='ram',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='rom',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='warranty',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='ram',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='rom',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='warranty',
            field=models.IntegerField(),
        ),
    ]
