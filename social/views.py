from django.shortcuts import render

# Create your views here.

#1st step
#from django.http import HttpResponse


#def home(request):
   # return HttpResponse("Hello maya")

#def home(request):

    
    #return render(request, "home.html")

#2nd step


from .models import Post

def home (request):
 posts = Post.objects.all()
    
 return render(request, "home.html", {
        "posts": posts
    })