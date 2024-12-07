from django.shortcuts import render, redirect
from blog.models import Blog
from django.utils.safestring import mark_safe
def home(request):
    blog = Blog.objects.all()
    for x in blog:
        x.description = mark_safe(x.description) 
    context = {
        "blogs": blog
    }
    return render(request,"blog/home.html", context)

def blog_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title and description:
            Blog.objects.create(title=title, description=description)
            return redirect('home')  
        else:
            error_message = "Başlık ve içerik gereklidir!"
            return render(request, 'home', {'error_message': error_message})

    return render(request,"blog/blogs.html")

def blog_details(request,slug):
    blog = Blog.objects.get(slug=slug)
    return render(request,"blog/blog_details.html",{
        "blog" : blog
    })
