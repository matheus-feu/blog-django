# Generated by Django 4.1.7 on 2023-03-08 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_author_post_alter_post_category_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_post',
            field=models.ImageField(default=1, upload_to='posts/%Y/%m/%d/', verbose_name='Imagem'),
            preserve_default=False,
        ),
    ]
