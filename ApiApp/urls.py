from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^api/movies$',views.movie_list),
    url(r'^api/movies/(?P<pk>[0-9]+)$', views.movie_detail)
]