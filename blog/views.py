from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post


# Create your views here.

def Index(request):
    return render(request, 'index.html')


class IndexView(ListView):
    print('12121212')
    template_name = 'index.html'
    model = Post

    def get(self, request, *args, **kwargs):
        context = {}
        posts = Post.objects.filter(status='published')
        context['posts'] = posts
        return render(request=request, template_name='index.html', context=context)

class PostDetailView(DetailView):
    template_name = 'single-post.html'
    model = Post

    def get(self, request, *args, **kwargs):
        if 'slug' in kwargs:
            slug = kwargs['slug']
            try:
                post = Post.objects.get(slug=slug)
            except:
                post = None
            context = {'post': post}
            return render(request, 'single-post.html', context)

class Contact(ListView):
    template_name = 'contact.html'
    model = Post

class About(ListView):
    template_name = 'about.html'
    model = Post

