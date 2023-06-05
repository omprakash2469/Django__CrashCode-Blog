from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from blogs.models import Blogs, Categories
from blogs.forms import CommentForm

def categoryDetails(request, slug):
    category = get_object_or_404(Categories, slug=slug)
    context = {
        "categories": category,
        "posts": category.blogs.filter(status=Blogs.ACTIVE)
    }
    return render(request, 'blogs.html', context)

def blogs(request):
    context = {
        "categories": Categories.objects.all
    }
    return render(request, 'category.html', context)

def blogDetails(request, category_slug, slug):
    post = get_object_or_404(Blogs, slug=slug, status=Blogs.ACTIVE)

    ## Handle user's comment
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post-details', category_slug=category_slug, slug=slug)
        
    context = {
        "post": post,
        "form": CommentForm()
    }
    return render(request, 'blogs_details.html', context)

def search(request):
    query = request.GET.get('query', '')
    result = Blogs.objects.filter(status=Blogs.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))
    context = {
        "query": query,
        "results": result
    }
    return render(request, 'search.html', context)