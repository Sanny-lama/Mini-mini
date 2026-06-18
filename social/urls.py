from django.urls import path
from . import views


urlpatterns = [

    path(
        "like/<int:id>/",
        views.like_post,
        name="like_post"
    ),


    path(
        "comment/<int:id>/",
        views.comment_post,
        name="comment_post"
    ),

]

