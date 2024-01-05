from django.shortcuts import render, redirect, get_object_or_404
from .form import *
from django.contrib.auth.decorators import login_required, permission_required
from .models import Post
from django.contrib.auth.models import User, Group


# Create your views here.
@login_required(login_url='/login')
def home(request, ordering=None):
    posts = Post.objects.all()
    if request.method == 'POST':
        post_id = request.POST.get('post-id')
        user_id = request.POST.get('user-id')

        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and (post.author == request.user or request.user.has_perm('main.delete_post')):
                post.delete()
        elif user_id:
            user = User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:

                if user.groups.filter(name="default").exists():
                    group = Group.objects.get(name="default")
                    group.user_set.remove(user)

                elif user.groups.filter(name="mod").exists():
                    group = Group.objects.get(name="mod")
                    group.user_set.remove(user)

    return render(request, 'main/home.html', {'posts': posts})


@login_required(login_url='/login')
@permission_required('main.add_post', login_url='/login', raise_exception=True)
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        print(form)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/home')
    else:
        form = PostForm()

    return render(request, 'main/post.html', {'form': form})


@login_required(login_url='/login')
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(post.id)
    print("test")
    if request.method == "POST":
        print(post)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            print('OK')
            return redirect('/home')
    else:
        form = PostForm(instance=post)

    ctx = {
        'form': form,
        'post': post
    }
    return render(request, 'main/post_edit.html', ctx)
    

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def post_ordering(request, ordering):
    if request.method == 'GET':
        order_method = ordering[9:]
        if order_method == 'latest':
            ordered_posts = Post.objects.order_by('-created_at')
        else:
            ordered_posts = Post.objects.order_by('created_at')

    return render(request, 'main/home.html', {'posts': ordered_posts})


def error_404_view(request, exception):
    return render(request, 'main/404.html')
