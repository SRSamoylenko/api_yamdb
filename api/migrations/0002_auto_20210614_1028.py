# Generated by Django 3.0.5 on 2021-06-14 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='titles',
            name='year',
            field=models.SmallIntegerField(help_text='Год выхода', null=True, verbose_name='Year'),
        ),
        migrations.AlterField(
            model_name='titles',
            name='title',
            field=models.CharField(help_text='Введи название', max_length=200, verbose_name='Name'),
        ),
    ]