
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pdf', models.FileField(upload_to='articles/')),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('REVIEW', 'Under Review'), ('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected'), ('PUBLISHED', 'Published')], default='PENDING', max_length=20)),
                ('submitted_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
