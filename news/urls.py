from django.conf.urls import include
from django.urls import path
from django.views.generic import ListView, DetailView
from .models import Articles
from django.conf.urls import url

urlpatterns = [
    url(r'^$',
        ListView.as_view(
            queryset=Articles.objects.all().order_by("-date")[:20],
            template_name="news/posts.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Articles, template_name="news/post.html"))
]
