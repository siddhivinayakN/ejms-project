from django.shortcuts import render, redirect
from .models import Article
from django.http import FileResponse
from reviews.models import Review
from django.contrib.auth.decorators import login_required

@login_required
def submit_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        pdf = request.FILES.get('pdf')

        Article.objects.create(
            title=title,
            pdf=pdf,
            author=request.user
        )

        return redirect('/admin/')

    return render(request, 'articles/submit_article.html')

from django.contrib.auth.decorators import login_required

@login_required

def my_articles(request):
    articles = Article.objects.filter(author=request.user)

    article_reviews = {}
    for article in articles:
        reviews = Review.objects.filter(article=article)
        article_reviews[article.id] = reviews

    return render(
        request,
        'articles/my_articles.html',
        {
            'articles': articles,
            'article_reviews': article_reviews
        }
    )


from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def change_status(request, article_id, status):
    article = Article.objects.get(id=article_id)
    article.status = status
    article.save()
    return redirect('/admin/')

def published_articles(request):
    articles = Article.objects.filter(status='PUBLISHED')
    return render(request, 'articles/published_articles.html', {'articles': articles})


def preview_pdf(request, article_id):
    article = Article.objects.get(id=article_id)
    return FileResponse(article.pdf.open(), content_type='application/pdf')
