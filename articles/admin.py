from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'status',
        'submitted_on'
    )

    list_filter = ('status','submitted_on')
    search_fields = ('title','author__username')
    ordering = ('-submitted_on',)
    actions = ['mark_under_review','mark_accepted','mark_rejected','mark_published']

    def mark_under_review(self,request,queryset):
        queryset.update(status='REVIEW')
    mark_under_review.short_description="Mark as Under Review"

    def mark_accepted(self,request,queryset):
        queryset.update(status='ACCEPTED')
    mark_accepted.short_description ="Mark as Accepted"

    def mark_rejected(self, request,queryset):
        queryset.update(status='REJECTED')
    mark_rejected.short_description="Mark as Rejected"

    def mark_published(self,request,queryset):
        queryset.update(status='PUBLISHED')
    mark_published.short_description= "Mark as Published"
