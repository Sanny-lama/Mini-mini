from django.db import models
from django.contrib.auth.models import User



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


    is_read = models.BooleanField(
        default=False
    )





    #bhatta ones
