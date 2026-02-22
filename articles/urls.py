from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_article, name='submit_article'),
    path('my/', views.my_articles, name='my_articles'),
    path('status/<int:article_id>/<str:status>/', views.change_status, name='change_status'),
    path('published/', views.published_articles, name='published_articles'),
    path('preview/<int:article_id>/', views.preview_pdf, name='preview_pdf'),

]
