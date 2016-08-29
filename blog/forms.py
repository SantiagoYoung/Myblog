from django import forms
from .models import *

class EditForm(forms.ModelForm):
    # title = forms.CharField(max_length=128)
    # author = forms.CharField(max_length=128)
    # text = forms.Textarea()
    # text = forms.CharField(widget=forms.Textarea)
    # category = forms.CharField(max_length=128)

    class Meta:
        model = Article
        fields = ('title','text','author','category','pubdate','update',)


# class ContactForm(forms.ModelForm):
#     subject = forms.CharField(max_length=128)
#     message = forms.CharField(widget=forms.Textarea)
#     sender = forms.EmailField()

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)



