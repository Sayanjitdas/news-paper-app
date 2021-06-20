from django.db import models
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'

class ArticleDetailView(DetailView): # new
    model = Article
    template_name = 'articles/article_detail.html'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'articles/article_new.html'
    fields = ('title', 'body', 'author',)

class ArticleUpdateView(UpdateView): # new
    model = Article
    fields = ('title', 'body',)
    template_name = 'articles/article_edit.html'

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('article_list')