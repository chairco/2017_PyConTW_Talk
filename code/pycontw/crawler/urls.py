# crawler/urls.py

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^crawler/$', views.crawler, name='crawler'),
    url(r'^task/(?P<id>\w+)$', views.view_task, name='view_task'),
]