# Generated by Django 3.0.5 on 2021-06-23 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210623_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, help_text='Введите категорию', max_length=200, verbose_name='Категория'),
        ),
    ]