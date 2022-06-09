from .models import Cu_comment, Gs25_comment, Seven_comment
from django import forms

class Cu_CommentForm(forms.ModelForm):
    class Meta:
        model = Cu_comment
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

class Gs25_CommentForm(forms.ModelForm):
    class Meta:
        model = Gs25_comment
        fields = ('content',)

class Seven_CommentForm(forms.ModelForm):
    class Meta:
        model = Seven_comment
        fields = ('content',)