from .models import Comment
from django.forms import ModelForm, Textarea


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

        widgets = {
            "body": Textarea(attrs={
                'class': 'form-control',
            }),
        }
