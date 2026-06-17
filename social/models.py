from django.db import models
from django.contrib.auth.models import User

#Interaction
#feeback page like system
from social.models import Post


class like(models.Model):
 user = models.Foreignkey(User, on_delete=models.CASCADE)
 post = models.Foreignkey(Post, on_delete=models.CASDCADE)

 created_at =models.DateTimeField(auto_now_add=True)





 #comment system
class Comment(models.Model):
 
 user=models.Foreignkey(User, on_delete=models.CASCADE)

 post=models.ForeignKey(Post, on_delete=models.CASCADE)
   
text=models.Textfield()
created_at =models.DateField(auto_now_add=True)