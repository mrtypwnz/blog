from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from webapp.models import Article, User, Rating, Comment
from webapp.forms import ArticleForm, ArticleUpdate, ArticleSearchForm, CommentForm, CommentUpdate
from django.urls import reverse_lazy



class ArticleListView(ListView, FormView):
    model = Article
    template_name = 'article_list.html'
    form_class = ArticleSearchForm

    def get_queryset(self):
        article_name = self.request.GET.get('article_name')
        if article_name:
            return self.model.objects.filter(article__icontains=article_name)
        else:
            return self.model.objects.all()



class ArticleCreateView(CreateView):
   model = Article
   form_class = ArticleForm
   template_name = 'article_create.html'
   success_url = reverse_lazy('article_list')

class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_update.html'
    success_url = reverse_lazy('article_list')

