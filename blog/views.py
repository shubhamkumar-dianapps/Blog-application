from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 3)  # 3 posts per page
    page_number = request.GET.get("page", 1)
    try:
        post = paginator.get_page(page_number)
    except EmptyPage:
        post = paginator.get_page(paginator.num_pages)
    except PageNotAnInteger:
        post = paginator.get_page(1)
    return render(request, "post/list.html", {"posts": post})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=slug,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )

    return render(request, "post/detail.html", {"post": post})
