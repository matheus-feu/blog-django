import os

from PIL import Image

from django.db import models
from django.conf import settings
from django.utils import timezone
from categorias.models import Category
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title_post = models.CharField(max_length=100, verbose_name='Título')
    author_post = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                                    verbose_name='Autor')  # Não apaga o usuário, mas pode ser nulo
    date_posted_post = models.DateTimeField(default=timezone.now, verbose_name='Data de publicação')
    content_post = models.TextField(verbose_name='Conteúdo')
    excerpt_post = models.TextField(verbose_name='Resumo', blank=True, null=True)
    # Não apaga a categoria, mas pode ser nulo, deixar o campo sem categoria
    category_post = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True,
                                      verbose_name='Categoria')
    image_post = models.ImageField(upload_to='posts/%Y/%m/%d/', verbose_name='Imagem')
    published_post = models.BooleanField(default=False, verbose_name='Publicado?')

    class Meta:
        verbose_name = 'Posts'
        verbose_name_plural = 'Postagens'

    def __str__(self):
        return self.title_post

    def save(self, *args, **kwargs):
        """Método para salvar a imagem do post"""
        super().save(*args, **kwargs)

        self.resize_image(self.image_post.name, 800)

    @staticmethod
    def resize_image(image_post, new_width):
        """Método para redimensionar a imagem do post,
        método fora da classe para não precisar instanciar a classe para usar o método"""

        # Path para a imagem
        img_path = os.path.join(settings.MEDIA_ROOT, image_post)

        # Abrir a imagem
        img = Image.open(img_path)
        width, height = img.size

        if width <= new_width:
            img.close()
            return

        # Arrendondar as dimensões
        new_height = round((new_width * height) / width)

        # Redimensionar a imagem
        new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
        new_img.save(img_path, optimize=True, quality=60)

        # Fechar a imagem
        new_img.close()



