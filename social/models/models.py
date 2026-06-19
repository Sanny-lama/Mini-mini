# from django.db import models
# from django.contrib.auth.models import User
 


# # Like System


# #Interaction
# #yo bananu ko karan mailey yo bitra socials bata nai post ko 
# # lagi import gardai xu so aauta class post banako ho
# class Post(models.Model):
#     title=models.CharField(max_length=100, default="No title")
# content=models.TextField()




# #feeback page like system

# class Post(models.Model):

#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE
#     )

#     content = models.TextField()

#     created_at = models.DateTimeField(
#         auto_now_add=True
#     )


#     def __str__(self):
#         return self.content[:20]


# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

 
# #comment system
# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
# =======
#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE
#     )

#     post = models.ForeignKey(
#         "Post",
#         on_delete=models.CASCADE
#     )

#     created_at = models.DateTimeField(
#         auto_now_add=True
#     )


#     class Meta:
#         unique_together = ('user','post')



# # Comment System

# class Comment(models.Model):

#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE
#     )

#     post = models.ForeignKey(
#         "Post",
#         on_delete=models.CASCADE
#     )

#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)


# #notification page
# class Notification(models.Model):
#     sender=models.ForeignKey(  User, on_delete=models.CASCADE,
# related_name="sender")
# receiver=models.ForeignKey(
# User, on_delete=models.CASCADE,
# related_name="receiver"
# )
# type=models.CharField(
# max_length=100    )  
# created_at=models.DateTimeField(auto_now_add=True)

#     created_at = models.DateTimeField(
#         auto_now_add=True
#     )



# # Notification System

# class Notification(models.Model):

#     sender = models.ForeignKey(
#         User,
#         related_name="sent_notifications",
#         on_delete=models.CASCADE
#     )

#     receiver = models.ForeignKey(
#         User,
#         related_name="notifications",
#         on_delete=models.CASCADE
#     )

#     type = models.CharField(
#         max_length=100
#     )

#     created_at = models.DateTimeField(
#         auto_now_add=True
# HEAD
#     )
    
#     # lalll

#     is_read = models.BooleanField(
#         default=False
#     )

# # Create your models here.


# # meee
# from django.db import models
# from django.contrib.auth import get_user_model
# from django.utils import timezone

# User = get_user_model()


# def post_image_upload_path(instance, filename):
#     return f"posts/{instance.author.id}/{filename}"


# class Post(models.Model):
#     author     = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
#     caption    = models.TextField(blank=True, verbose_name="Caption") 
#     image      = models.ImageField(upload_to=post_image_upload_path, blank=True, null=True)
#     location   = models.CharField(max_length=150, blank=True)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ["-created_at"]
#         verbose_name = "Post"
#         verbose_name_plural = "Posts"

#     def __str__(self):
#         preview = self.caption[:40] if self.caption else "(no caption)"
#         return f"[{self.author.username}] {preview}"

#     def has_image(self):
#         return bool(self.image and self.image.name)

#     def was_edited(self):
#         delta= self.updated_at - self.created_at return delta.total_seconds() > 5


from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils import timezone
User = get_user_model()


class Post(models.Model):
    title=models.CharField(max_length=100, default="No title")
    content=models.TextField()




#feeback page like system

class Post(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    caption = models.TextField(
        blank=True
    )


    def __str__(self):
        return self.content[:20]


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


#comment system
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

#comment system
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    location = models.CharField(
        max_length=150,
        blank=True
    )

    created_at = models.DateTimeField(
        default=timezone.now
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        preview = self.caption[:40] if self.caption else "(no caption)"
        return f"[{self.author.username}] {preview}"

    def has_image(self):
        return bool(self.image and self.image.name)

# Comment System

class Comment(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    post = models.ForeignKey(
        "Post",
        on_delete=models.CASCADE
    )


    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



#notification page
class Notification(models.Model):
    sender=models.ForeignKey(  User, on_delete=models.CASCADE,
related_name="sender")
receiver=models.ForeignKey(
User, on_delete=models.CASCADE,
related_name="receiver"
)
type=models.CharField(
max_length=100    )  
created_at=models.DateTimeField(auto_now_add=True)


#notification page
class Notification(models.Model):
    sender=models.ForeignKey(  User, on_delete=models.CASCADE,
related_name="sender")
receiver=models.ForeignKey(
User, on_delete=models.CASCADE,
related_name="receiver"
)
type=models.CharField(
max_length=100    )  
created_at=models.DateTimeField(auto_now_add=True)




# Notification System

class Notification(models.Model):

    sender = models.ForeignKey(
        User,
        related_name="sent_notifications",
        on_delete=models.CASCADE
    )

    receiver = models.ForeignKey(
        User,
        related_name="notifications",
        on_delete=models.CASCADE
    )

    type = models.CharField(
        max_length=100
    )

    created_at = models.DateTimeField(
        auto_now_add=True

    )

    # lalll

    is_read = models.BooleanField(
        default=False
    )

