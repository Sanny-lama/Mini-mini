from django.db import models
from django.contrib.auth.models import User

<<<<<<< HEAD
#Interaction
#yo bananu ko karan mailey yo bitra socials bata nai post ko 
# lagi import gardai xu so aauta class post banako ho
class Post(models.Model):
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title=models.CharField(
        max_length=100,
        default="No title"
    )

    content=models.TextField()

    created_at=models.DateTimeField(
        auto_now_add=True
    )


#feeback page like system

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

 #comment system
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


#notification page
class Notification(models.Model):
 sender=models.ForeignKey(
  User, on_delete=models.CASCADE,
  related_name="sender")
 
 receiver=models.ForeignKey(
  User, on_delete=models.CASCADE,
  related_name="receiver"
 )


type=models.CharField(
 max_length=100    )
  

created_at=models.DateTimeField(auto_now_add=True)





=======
# 1. USER PROFILE TABLE
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, default="Securely share your Nepali moments.")
    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Profile"


# 2. UPDATED POST TABLE
class Post(models.Model):
    # Connects each post to a registered user from your login system
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    
    # Stores the image link for the mountain or food assets
    image_url = models.URLField(max_length=500, default="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=600")
    
    # Serves as your caption/description text
    content = models.TextField()
    
    # Tracks likes safely on the database side
    likes_count = models.IntegerField(default=0)
    
    # Automatically saves the date and time when shared
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Shows the author name and a small preview of the text in the admin dashboard
        return f"Post by {self.author.username} - {self.content[:20]}..."
    


    #shanti ones



class Post(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.content[:20]

class Like(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:
        unique_together = ('user','post')




class Comment(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )

    text = models.TextField()


    created_at = models.DateTimeField(
        auto_now_add=True
    )




class Follow(models.Model):

    follower = models.ForeignKey(
        User,
        related_name="following",
        on_delete=models.CASCADE
    )

    following = models.ForeignKey(
        User,
        related_name="followers",
        on_delete=models.CASCADE
    )




class Notification(models.Model):

    receiver = models.ForeignKey(
        User,
        related_name="notifications",
        on_delete=models.CASCADE
    )


    sender = models.ForeignKey(
        User,
        related_name="sent_notifications",
        on_delete=models.CASCADE
    )


    message = models.CharField(
        max_length=255
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )
    # lalll

    is_read = models.BooleanField(
        default=False
    )
>>>>>>> afd5c999b49f1edd481f6443d620ea25a4e62a4c
