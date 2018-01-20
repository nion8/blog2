# from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
# from django.http import HttpResponse
from django.views import View
from .models import Post
from user_profile.models import User
from posts.forms import PostForm


#
# def home(request):
#     return render(request, 'home.html', {})


class Index(View):

    def get(self, request):
        context = {'text': 'Привет Мир!!'}
        return render(request, 'home.html', context)


class Profile(View):
    # user profile Page http://127.0.0.1:8000/user/<username>
    def get(self, request, username):
        user = User.objects.get(username=username)
        posts = Post.objects.filter(user=user)
        form = PostForm()
        context = {
            'posts': posts,
            'user': user,
            'form': form,
        }
        return render(request, 'profile.html', context)


