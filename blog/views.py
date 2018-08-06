from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Project
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.models import User

def index_page(request):
    return render(request, 'blog/index.html')

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'blog/project_list.html', {'projects':projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'blog/project_detail.html',{'project':project})

# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-created_date')
#     return render(request, 'blog/post_list.html', {'posts':posts})
#     #reder function(request, html name, 매개변수)

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.get(username='yoon')
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.get(username='yoon')
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
