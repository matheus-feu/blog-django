from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.db.models import Q, Count, Case, When

from django.contrib import messages
from comentarios.forms import CommentForm
from comentarios.models import Comments
from .models import Post


# Create your views here.
class PostIndexView(ListView):
    """Classe mãe vão herdar de ListView e terão as funcionalidades básicas de listagem
    de objetos já implementadas, simplificando o desenvolvimento de views."""

    model = Post
    template_name = 'posts/index.html'
    paginate_by = 6
    context_object_name = 'posts'

    def get_queryset(self):
        """Faz a consulta e retorna os posts ordernados por id e injetar o número de comentários,
        Post será publicado se o campo published_post for True"""

        qs = super().get_queryset()
        qs = qs.select_related('category_post')  # Faz a consulta de categoria
        qs = qs.order_by('-id').filter(published_post=True)
        qs = qs.annotate(
            # Anotação para contar os comentários
            num_comments=Count(
                Case(
                    When(comments__published_com=True, then=1)  # Quando o comentário for publicado, então conta 1.
                )
            )
        )

        return qs


class PostCategoryView(PostIndexView):
    """É possível visualizar os posts por categoria no Django, por meio da herança da classe mãe PostIndexView.
    Ao fazer isso, é permitido que o usuário visualize os posts por categoria em uma única página, utilizando a classe ListView.
    Dessa forma, a organização dos posts é facilitada e a experiência do usuário é aprimorada."""

    template_name = 'posts/post_category.html'

    def get_queryset(self):
        """Retorna os posts por categoria"""
        qs = super().get_queryset()

        categoria = self.kwargs.get('categoria', None)

        if not categoria:
            return qs

        # Faz a busca por categoria
        qs = qs.filter(category_post__name_cat__iexact=categoria)  # iexact = case insensitive

        return qs


class PostSearchView(PostIndexView):
    """A classe PostSearchView é responsável por realizar a busca de posts no site.
    Também herdando da classe mãe PostIndexView"""

    template_name = 'posts/post_search.html'

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')

        if not termo:
            return qs

        # Faz a busca por título, autor, conteúdo, resumo e categoria
        qs = qs.filter(
            Q(title_post__icontains=termo) |
            Q(author_post__first_name__iexact=termo) |
            Q(content_post__icontains=termo) |
            Q(excerpt_post__icontains=termo) |
            Q(category_post__name_cat__icontains=termo)
        )

        return qs


class PostDetailView(View):
    """Classe responsável por exibir os detalhes do post,
    como título, autor, conteúdo, resumo, data de publicação, etc."""

    template_name = 'posts/post_detail.html'

    def setup(self, request, *args, **kwargs):
        """Método que é executado antes de qualquer outro método da classe"""

        super().setup(request, *args, **kwargs)

        pk = self.kwargs.get('pk', None)
        post = get_object_or_404(Post, pk=pk, published_post=True)
        comments = Comments.objects.filter(post_com=pk, published_com=True)

        self.context = {
            'post': post,
            'comments': comments,
            'form': CommentForm(request.POST or None),
        }

    def get(self, request, *args, **kwargs):
        """Método responsável por exibir os detalhes do post"""

        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        """Método responsável por salvar o formulário de comentários"""

        # Checa se o formulário é válido
        form = self.context['form']

        if not form.is_valid():
            messages.error(request, 'Erro ao enviar comentário!')
            return render(request, self.template_name, self.context)

        # Salva o comentário
        comment = form.save(commit=False)

        # Checa se o usuário está logado ou não, permitindo que ele comente como anônimo ou logado.
        if request.user.is_authenticated:
            comment.user_com = request.user

        # Relaciona o comentário com o post e salva ele no banco de dados
        comment.post_com = self.context['post']
        comment.save()
        messages.success(request, 'Seu comentário foi enviado para a revisão.')

        return redirect('posts:post_detail', pk=self.kwargs.get('pk'))

