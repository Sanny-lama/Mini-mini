
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Like, Comment, Notification


#like post
@login_required
def like_post(request, id):

    post = get_object_or_404(
        Post,
        id=id
    )


    like, created = Like.objects.get_or_create(
        user=request.user,
        post=post
    )


    if created:
        Notification.objects.create(
            sender=request.user,
            receiver=post.user,
            type="liked your post"
        )


    return redirect("home")


#comment post    
@login_required
def comment_post(request, id):

    post = get_object_or_404(
        Post,
        id=id
    )


    if request.method == "POST":

        text = request.POST.get("comment")


        if text and text.strip():

            Comment.objects.create(
                user=request.user,
                post=post,
                text=text.strip()
            )


            Notification.objects.create(
                sender=request.user,
                receiver=post.user,
                type="commented on your post"
            )


    return redirect("home")
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# HOME (after login)
def home(request):
    return render(request, 'home.html')


# REGISTER
def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return redirect('login')    

    return render(request, 'register.html')


# LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')


from django.shortcuts import render

def home(request):
    return render(request, 'home.html')



# meeeeee
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden
from django.db.models import Q

from .models import Post
from .forms import PostForm


@login_required
def home(request):
    search_query = request.GET.get("q", "").strip()

    if search_query:
        all_posts = Post.objects.select_related("author").filter(
            Q(caption__icontains=search_query) |
            Q(author__username__icontains=search_query) |
            Q(location__icontains=search_query)
        )
    else:
        all_posts = Post.objects.select_related("author").all()

    paginator   = Paginator(all_posts, 10)
    page_number = request.GET.get("page", 1)
    page_obj    = paginator.get_page(page_number)

    user_posts   = Post.objects.filter(author=request.user).order_by("-created_at")[:8]
    recent_posts = Post.objects.select_related("author").order_by("-created_at")[:10]

    context = {
        "posts":        page_obj,
        "user_posts":   user_posts,
        "recent_posts": recent_posts,
        "search_query": search_query,
    }
    return render(request, "home.html", context)


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post        = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Your post has been published!")
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "create_post.html", {"form": form})


@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            updated_post = form.save(commit=False)
            if request.POST.get("clear_image"):
                if updated_post.image:
                    updated_post.image.delete(save=False)
                updated_post.image = None
            updated_post.save()
            messages.success(request, "Your post has been updated!")
            return redirect("home")
    else:
        form = PostForm(instance=post)
    return render(request, "edit_post.html", {"form": form, "post": post})


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")

    if request.method == "POST":
        if post.image:
            post.image.delete(save=False)
        post.delete()
        messages.success(request, "Your post has been deleted.")
        return redirect("home")
    return render(request, "delete_post.html", {"post": post})


