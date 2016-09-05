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


class ContactForm(forms.Form):
    name = forms.CharField(max_length=128, required=True)
    email = forms.EmailField(required=True)
    content = forms.CharField(
        widget=forms.Textarea,
        required=True
    )
    subject = forms.CharField(max_length=128, required=True)

    # def __init__(self, *args, **kwargs):
    #     super(ContactForm, self).__init__(*args, **kwargs)
    #     self.fields['name'].label = 'Your name:'
    #     self.fields['email'].label = 'Your email:'
    #     self.fields['content'].label = 'Say something.'
    #     self.fields['subject'].label = 'Subject:'