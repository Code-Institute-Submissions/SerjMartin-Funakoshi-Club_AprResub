from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ('body',)
