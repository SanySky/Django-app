from django import forms

from blogapp.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "title", "pub_date", "author", "category", "tags"
