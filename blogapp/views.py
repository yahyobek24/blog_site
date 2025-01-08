from gc import get_objects

from django.shortcuts import render

from .models import Post
from django.views.generic import ListView

class PstListWiews(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 5
    template_name = "blog/post/list.html"




def post_detail(request, year, month, day, slug, get_objects_or_404=None):
    post = get_objects_or_404(Post, slug=slug, status= "published", publish__yead=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post' : post})