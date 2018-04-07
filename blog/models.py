from django.db import models

# Create your models here.
# 博文模型
class Article(models.Model):
    article_title = models.CharField(max_length=300)
    article_text = models.TextField(max_length=5000)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    def __str__(self):
        return self.article_text
