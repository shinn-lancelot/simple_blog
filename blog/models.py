from django.db import models

# Create your models here.
class Article(models.Model):
    article_title = models.CharField(max_length=300)
    article_text = models.CharField(max_length=5000)
    create_time = models.DateTimeField(True)
    update_time = models.DateTimeField(True)