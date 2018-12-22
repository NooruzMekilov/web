from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from mysite.views import  IndexView, NewsView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^news/', NewsView.as_view(), name="news"),
    path('admin/', admin.site.urls),
]
