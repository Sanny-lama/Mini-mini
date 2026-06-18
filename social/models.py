from django.db import models
from django.contrib.auth.models import User

#Interaction
#yo bananu ko karan mailey yo bitra socials bata nai post ko 
# lagi import gardai xu so aauta class post banako ho
class Post(models.Model):
    title=models.CharField(max_length=100, default="No title")
content=models.TextField()



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
    sender=models.ForeignKey(  User, on_delete=models.CASCADE,
related_name="sender")
receiver=models.ForeignKey(
User, on_delete=models.CASCADE,
related_name="receiver"
)
type=models.CharField(
max_length=100    )  
created_at=models.DateTimeField(auto_now_add=True)