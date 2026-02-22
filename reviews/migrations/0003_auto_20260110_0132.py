
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0002_article_author'),
        ('reviews', '0002_review_reviewer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='comment',
            new_name='comments',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='review_date',
            new_name='reviewed_on',
        ),
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
        migrations.AddField(
            model_name='review',
            name='recommendation',
            field=models.CharField(choices=[('ACCEPT', 'Accept'), ('REJECT', 'Reject'), ('REVISION', 'Needs Revision')], default='REVISION', max_length=10),
        ),
        migrations.AlterField(
            model_name='review',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='articles.Article'),
        ),
        migrations.AlterField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
