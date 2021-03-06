# from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
# from django.http import HttpResponse
from django.views import View
from .models import Post, HashTag
from user_profile.models import User
from posts.forms import PostForm
from django.http import HttpResponseRedirect


#
# def home(request):
#     return render(request, 'home.html', {})


class Index(View):

    def get(self, request):
        context = {'text': 'Посты по Django!!'}
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


class PostPost(View):
    def post(self, request, username):
        form = PostForm(self.request.POST)
        if form.is_valid():
            user = User.objects.get(username=username)
            post = Post(text=form.cleaned_data['text'], user=user)
            post.save()
            words = form.cleaned_data['text'].split(" ")
            for word in words:
                if word.startswith('#'):
                    hash_tag, created = HashTag.objects.get_or_create(name=word)
                    hash_tag.post.add(post)
        return HttpResponseRedirect('/user/' + username)
