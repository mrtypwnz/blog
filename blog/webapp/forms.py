from django import forms
from webapp.models import Article, Comment


class ArticleSearchForm(forms.Form):
    article_name = forms.CharField(max_length=200, required=False, label='Название статьи')


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'comment', 'created_at']


class ArticleUpdate(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'comment']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'article', 'text']


class CommentUpdate(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']