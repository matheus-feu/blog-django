from django.forms import ModelForm

from .models import Comments


class CommentForm(ModelForm):
    """Formulário de comentários"""
    def clean(self):
        cleaned_data = super(CommentForm, self).clean()
        name_com = cleaned_data.get('name_com')
        email_com = cleaned_data.get('email_com')
        comment = cleaned_data.get('comment')

        if not name_com and not email_com and not comment:
            self.add_error('name_com', 'Você precisa preencher pelo menos um campo')
            self.add_error('email_com', 'Você precisa preencher pelo menos um campo')
            self.add_error('comment', 'Você precisa preencher pelo menos um campo')

        if email_com:
            if '@' not in email_com:
                self.add_error('email_com', 'Email inválido')

        if name_com:
            if any(char.isdigit() for char in name_com):
                self.add_error('name_com', 'Não é permitido números no nome')

    class Meta:
        model = Comments
        fields = ['name_com', 'email_com', 'comment']
