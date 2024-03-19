from django.urls import path
from .import views


urlpatterns = [
    path('',views.HomeListView.as_view(),name='home-page'),
    path('articles',views.ArticleListView.as_view(),name='all-posts'),
    path("save-article",views.SaveView.as_view(),name="save-article"),
    path('posts/<slug:slug>',views.ArticleDetailView.as_view(),name='post-detail-page'),
    
]