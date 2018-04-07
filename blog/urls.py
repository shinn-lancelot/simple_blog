from django.urls import path
from . import views
# url命名空间
app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.article, name='article')
]
