from .models import Comment
from django import forms
from allauth.account.forms import LoginForm

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        labels = {
            'content': (''),
        }
        widgets = {
                    'content': forms.Textarea(
                        attrs={
                            'class': 'form-control',
                            'style': 'width: 100%; height: 6.25em; resize: none;',
                        }
                    ),
                }

class LoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["login"].label = ""
        self.fields["password"].label = ""