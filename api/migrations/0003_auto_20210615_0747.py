# Generated by Django 3.0.5 on 2021-06-15 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210614_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.CharField(max_length=50, null=True, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='title',
            name='category',
            field=models.IntegerField(blank=True, verbose_name='Категория'),
        ),
    ]