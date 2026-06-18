from django.db import models
from django.contrib.auth.models import User


# Like System

class Like(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    post = models.ForeignKey(
        "Post",
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:
        unique_together = ('user','post')



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


    created_at = models.DateTimeField(
        auto_now_add=True
    )



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