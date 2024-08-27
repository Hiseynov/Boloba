# forms.py
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'coments']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Your Name ...','maxlength': '50'}) ,
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'coments': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Coments'}),
        }
        labels = {
            'name': 'Your Name',
            'email': 'E-Mail Address',
            'coments': 'Comment',
        }
        error_messages = {
            'name': {
                'required': 'Doldurmag mutlegdir',
                'max_length': 'Name cannot be longer than 50 characters.'
            },
            'email': {
                'required': 'This field is required.',
                'invalid': 'Enter a valid email address.'
            },
            'coments': {
                'required': 'This field is required.'
            }
        }

