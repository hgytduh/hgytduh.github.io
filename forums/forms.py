from django import forms
from django.forms import ModelForm
from forums.models import Post, Reply


class PostForm(ModelForm):
    title = forms.CharField(label=(u'Title'))
    text = forms.CharField(label=(u'Text'), widget=forms.Textarea())

    class Meta:
        model = Post
        exclude = []


class ReplyForm(ModelForm):
    title = forms.CharField(label=(u'Title'))
    text = forms.CharField(label=(u'Text'), widget=forms.Textarea())
    exclude = []

    class Meta:
        model = Reply
        exclude = []
