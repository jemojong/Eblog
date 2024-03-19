from typing import Any
from django.shortcuts import render,get_object_or_404
from .models import Article,Rating,Author
from django.views.generic.list import ListView
from django.views import View
from .forms import ThoughtsForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

class HomeListView(ListView):
    model=Article
    template_name = 'blog/index.html'
    ordering = ["-date"]
    context_object_name ="articles"

    def get_queryset(self):
        queryset= super().get_queryset()
        data = queryset[:3]
        return data
    

# def home_page(requests):
#     latest_articles = Article.objects.all().order_by("-date")[:3 ]
#     return render(requests,'blog/index.html',)

class ArticleListView(ListView):
    model = Article
    template_name = "blog/all_posts.html"
    ordering = ["-date"]
    context_object_name = "articles"


class ArticleDetailView(View):
    def get(self,request,slug):
        article = Article.objects.get(slug=slug)
        is_saved_later =article.id in request.session['saved_article']
        
        context={
            "article":article,
            "rating": article.rating.all(),
            "form":ThoughtsForm(),
            "thoughts":article.thoughts.all().order_by("-id"),
            "is_saved":is_saved_later
        }

        return render(request, "blog/post-detail.html",context)
    
    def post(self,request,slug):
        article = Article.objects.get(slug=slug)
        form = ThoughtsForm(request.POST)
        if form.is_valid():
            thought=form.save(commit=False)
            thought.article = article
            thought.save()
            return HttpResponseRedirect(reverse('post-detail-page',args=[slug]))
        article = Article.objects.get(slug=slug)
        context={
            "article":article,
            "rating": article.rating.all(),
            "form":form,
            "thoughts":article.thoughts.all().order_by("-id")
        }
        
        return render(request, "blog/post-detail.html",context)
    
class SaveView(View):
    def get(self,request):
        saved_articles = request.session.get("saved_article")
        context={}
        if saved_articles is None:
            context["article"]=[]
            context["has_article"]=False
          
        else:
            articles =Article.objects.filter(id__in=saved_articles)
            context["articles"]=articles
            context["has_article"] = True
            
            print(articles)
        return render(request, "blog/saved-posts.html",context)


    def post(self,request):
        saved_article = request.session.get("saved_article")

        print(saved_article)
        article = int(request.POST["article_id"])
        if saved_article is None:
            saved_article=[]
            
        if article not in saved_article:
            saved_article.append(article)
            
        else:
             saved_article.remove(article)
        request.session['saved_article'] =saved_article
            
        return HttpResponseRedirect("/")


    # def get_context_data(self, **kwargs):
    #     context= super().get_context_data(**kwargs)
    #     context["rating"] = self.object.rating.all()
    #     context["form"]=ThoughtsForm()
    #     return context

# def post_detail(request,slug):
#     indentified_article = get_object_or_404(Article,slug=slug)
    
#     return render(request,"blog/post-detail.html",{"article":indentified_article,"rating":indentified_article.rating.all()})