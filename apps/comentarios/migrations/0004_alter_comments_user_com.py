# Generated by Django 4.1.7 on 2023-03-09 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comentarios', '0003_alter_comments_post_com'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='user_com',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Usuário comentário'),
        ),
    ]
