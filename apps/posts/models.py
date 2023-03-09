from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

from categorias.models import Category


# Create your models here.
class Post(models.Model):
    title_post = models.CharField(max_length=100, verbose_name='Título')
    author_post = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor') # Não apaga o usuário, mas pode ser nulo
    date_posted_post = models.DateTimeField(default=timezone.now, verbose_name='Data de publicação')
    content_post = models.TextField(verbose_name='Conteúdo')
    excerpt_post = models.TextField(verbose_name='Resumo', blank=True, null=True)
    # Não apaga a categoria, mas pode ser nulo, deixar o campo sem categoria
    category_post = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Categoria')
    image_post = models.ImageField(upload_to='posts/%Y/%m/%d/', verbose_name='Imagem')
    published_post = models.BooleanField(default=False, verbose_name='Publicado?')

    class Meta:
        verbose_name = 'Posts'
        verbose_name_plural = 'Postagens'

    def __str__(self):
        return self.title_post
