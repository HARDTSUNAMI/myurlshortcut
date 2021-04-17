from django import forms
# from django.core.validators import URLValidator
from django.forms import TextInput
from django.core.exceptions import ValidationError
from .models import LinkModel


class LoginForm(forms.Form):
    username = forms.CharField(max_length=25, label="Login", )
    password = forms.CharField(max_length=30, label='Password',
                               widget=forms.PasswordInput)


class LinkForm(forms.ModelForm):
    class Meta:
        model = LinkModel
        fields = ['link',
                  ]
        widgets = {
            'link': TextInput(attrs={'class': 'formstyle'})

        }

    def clean_link(self):
        link = self.cleaned_data.get('link')
        matches = ['http:', 'https:', 'ftp:', 'ftps:']
        print(link)
        if any(x in link for x in matches):
            return link
        else:
            raise ValidationError(message='ENTER VALID URL')
