from django.urls import path
from . import views
# url命名空间
app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),
]
