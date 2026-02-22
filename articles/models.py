from django.db import models
from users.models import User

class Article(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('REVIEW', 'Under Review'),
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected'),
        ('PUBLISHED', 'Published'),
    )

    title = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='articles/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )
    submitted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
