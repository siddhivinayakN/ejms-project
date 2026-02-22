from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import Review
from articles.models import Article


# REVIEW ARTICLE

@login_required
@staff_member_required
def review_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if Review.objects.filter(article=article, reviewer=request.user).exists():
        return redirect('/reviews/dashboard/')

    if request.method == 'POST':
        comments = request.POST.get('comments')
        recommendation = request.POST.get('recommendation')

        Review.objects.create(
            article=article,
            reviewer=request.user,
            comments=comments,
            recommendation=recommendation
        )

        if recommendation == 'ACCEPT':
            article.status = 'ACCEPTED'
        elif recommendation == 'REJECT':
            article.status = 'REJECTED'
        else:
            article.status = 'REVIEW'

        article.save()
        return redirect('/reviews/dashboard/')

    return render(request, 'reviews/review_article.html', {'article': article})



# REVIEWER DASHBOARD

@login_required
@staff_member_required
def reviewer_dashboard(request):
    reviewed_ids = Review.objects.filter(
        reviewer=request.user
    ).values_list('article_id', flat=True)

    articles = Article.objects.exclude(id__in=reviewed_ids)

    return render(
        request,
        'reviews/reviewer_dashboard.html',
        {'articles': articles}
    )
