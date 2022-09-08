from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404
from portal.models import HomepageBlog


def guide_home(request):
    portal_obj = HomepageBlog.objects.filter(app="guide",status="Published")
    context = {"portal_obj":portal_obj.first() if portal_obj else None}
    return render(request,'guide/blog_home.html',context)

def guide_blog(request,url):
    url_slug = url
    blog_obj = get_object_or_404(Blog, url_slug = url_slug, status="Published")
    context = {'blog_obj':blog_obj}
    return render(request,'guide/guide_blog.html',context)


