# from django.urls import
from django.conf.urls import url
from posts.views import Index, Profile

# from . import views
from posts import views

urlpatterns = [
    # path('', views.Index, name='index'),
    # path('', Index.as_view(), name='index'),
    # path('', views.index, name='index'),
    #     path('', views.blog, name='blog'),
    # path('', Profile.as_view()),
    # re_path(r'^user/(\w+)/$', views.Profile, name='profile'),
    # url(r'^user/', Profile.as_view(), name='profile')
]
