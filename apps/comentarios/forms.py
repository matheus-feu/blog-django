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
            raise forms.ValidationError('Você precisa preencher pelo menos um campo')
        if email_com:
            if '@' not in email_com:
                raise forms.ValidationError('E-mail inválido')
        if name_com:
            if any(char.isdigit() for char in name_com):
                raise forms.ValidationError('Nome inválido')

    class Meta:
        model = Comments
        fields = ['name_com', 'email_com', 'comment']
