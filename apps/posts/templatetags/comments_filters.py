from django import template

register = template.Library()


@register.filter(name='filter_count_comments')
def filter_count_comments(comments):
    """Retorna a quantidade de comentários do post"""
    try:
        if comments.count() == 0:
            return f'Nenhum comentário'
        elif comments.count() == 1:
            return f'{comments.count()} comentário'
        else:
            return f'{comments.count()} comentários'
    except:
        return f'{comments.count()} comentários'
