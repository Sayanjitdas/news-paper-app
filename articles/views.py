from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'

class ArticleDetailView(LoginRequiredMixin,DetailView): # new
    model = Article
    template_name = 'articles/article_detail.html'
    login_url = 'login'

class ArticleCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Article
    template_name = 'articles/article_new.html'
    fields = ('title', 'body')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView): # new
    model = Article
    fields = ('title', 'body',)
    template_name = 'articles/article_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user