# Generated by Django 4.1.7 on 2023-03-07 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categorias', '0003_alter_category_name_cat'),
        ('posts', '0002_alter_post_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='categorias.category', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_post',
            field=models.TextField(verbose_name='Conteúdo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted_post',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de publicação'),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerpt_post',
            field=models.TextField(blank=True, null=True, verbose_name='Resumo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_post',
            field=models.ImageField(blank=True, null=True, upload_to='posts/%Y/%m/%d/', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_post',
            field=models.BooleanField(default=False, verbose_name='Publicado?'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_post',
            field=models.CharField(max_length=100, verbose_name='Título'),
        ),
    ]
