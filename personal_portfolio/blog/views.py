from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from blog.models import Blog


# Create your views here.
def blog(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
