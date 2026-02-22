from django.db import models
from django.conf import settings
from articles.models import Article

class Review(models.Model):

    RECOMMENDATION_CHOICES = [
        ('ACCEPT', 'Accept'),
        ('REJECT', 'Reject'),
        ('REVISION', 'Needs Revision'),
    ]

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    reviewer = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    limit_choices_to={'is_staff': True}
)

    comments = models.TextField()
    recommendation = models.CharField(
    max_length=10,
    choices=RECOMMENDATION_CHOICES,
    default='REVISION'
)


    reviewed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.article.title} - {self.recommendation}"
