from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

from posts.models import Post


# Create your models here.
class Comments(models.Model):
    name_com = models.CharField(max_length=50, verbose_name='Nome comentário')
    email_com = models.EmailField(verbose_name='E-mail comentário')
    comment = models.TextField(verbose_name='Comentário')
    # Quando um post for deletado, os comentários também serão.
    post_com = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post comentário', related_name='comments')
    # Quando um usuário for deletado, os artigos e comentários não serão.
    user_com = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Usuário comentário', blank=True, null=True)
    date_com = models.DateTimeField(default=timezone.now, verbose_name='Data comentário')
    published_com = models.BooleanField(default=False, verbose_name='Publicar comentário?')

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

    def __str__(self):
        return self.name_com

