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

from . import views 

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
]

