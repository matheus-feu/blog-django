# Generated by Django 4.1.7 on 2023-03-07 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name_cat',
            field=models.CharField(max_length=50, verbose_name='Nome da categoria'),
        ),
    ]