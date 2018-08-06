from django.conf.urls import url
from . import views

#blog/urls.py에서 해당 뷰를 가져와서 url에 연결한다.
urlpatterns = [
    url(r'^$', views.index_page, name='index_page'),
    url(r'^project/(?P<pk>\d+)/$', views.project_detail, name='project_detail'),

    # url(r'^post/(?P<pk>\d+)/$', views.post_detail, name ='post_detail'),
    # url(r'^post/new/$', views.post_new, name='post_new'),
    # url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]
