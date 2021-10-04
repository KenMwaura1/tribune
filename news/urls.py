from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.welcome, name='home'),
    url('^today/$',views.news_of_day,name='newsToday')
]
