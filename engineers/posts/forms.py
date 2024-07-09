from django import forms
from .models import Post, Comment


class CRUDFORM(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "title"})
    )
    post_type = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "type"})
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "description"}
        )
    )
    image = forms.ImageField()

    class Meta:
        model = Post
        fields = ["title", "post_type", "description", "image"]


class CommentForm(forms.ModelForm):
    content = forms.Textarea(attrs={"class": "form-control", "placeholder": "content"})

    class Meta:
        model = Comment
        fields = ["content"]
