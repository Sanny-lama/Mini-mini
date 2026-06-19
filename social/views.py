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
