from django import forms
from django.forms import ModelForm
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','image','videolink','fav','text',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'image':forms.FileInput(attrs={'class':'btn'}),
            'videolink':forms.URLInput(attrs={'class': 'form-control','placeholder': 'VideoLink'}),
            'fav':forms.CheckboxInput(),
            'text':forms.Textarea(attrs={'class': 'form-control','cols':20, 'rows':3, 'placeholder': 'Query'}),

        }

class contactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}))
    subject = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    message = forms.CharField(required=True,widget=forms.Textarea(attrs={'class': 'form-control','cols':20, 'rows':3, 'placeholder': 'Query'}))
