from django.http import HttpResponse
from django.template import loader
from .models import Usern, Post, Comment, Category

def base(request):
  template = loader.get_template('base.html')
  return HttpResponse(template.render())

def users(request):
    myusers = Usern.objects.all().values()
    template = loader.get_template('users.html')
    context = {
      'myusers': myusers,
    }
    return HttpResponse(template.render(context, request))

def Posts(request):
    mypost = Post.objects.all().values()
    template = loader.get_template('blogs.html')
    context = {
        'mypost': mypost,
    }
    return HttpResponse(template.render(context, request))

def comments(request):
    mycomment = Comment.objects.all().values()
    template = loader.get_template('comments.html')
    context = {
        'mycomment': mycomment,
    }
    return HttpResponse(template.render(context, request))

def categories(request):
    mycategory = Category.objects.all().values()
    template = loader.get_template('categories.html')
    context = {
        'mycategory': mycategory,
    }
    return HttpResponse(template.render(context, request))

def blogdetails(request, ID):
    theblogdetails = Post.objects.get(ID=ID)
    template = loader.get_template('blogdetails.html')
    context = {
        'theblogdetails': theblogdetails,
    }
    return HttpResponse(template.render(context, request))