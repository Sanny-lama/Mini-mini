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