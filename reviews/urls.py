from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.reviewer_dashboard, name='reviewer_dashboard'),
    path('submit/<int:article_id>/', views.review_article, name='review_article'),
]
