from re import I
from django.shortcuts import render
import json
from portal.models import *;
# dictionary to store the urls and its respective numbers
global stories 
stories={}

#home page 
def homepage(request):
    # portal_obj = HomepageBlog.objects.filter(app="web-stories",status="Published")
    # context = {"portal_obj":portal_obj.first() if portal_obj else None}
    file=open('media/web-stories/title-description.json')
    data=json.load(file)
    
    context={}
    
    
    context['titles']=data
    print("*************************************************************************")
    print(context)
    return render(request,'web_stories/home.html',context)

#web stories
# def webstories(request,story):
#     context={}
#     file=open('media/web-stories/title-description.json')
#     data=json.load(file)
#     webno=story
#     file=open('media/web-stories/webstory-'+str(webno)+"/webstory-"+str(webno)+".json")
#     data=json.load(file)
#     context['data']=data
#     context['webno']=webno
#     file=open('media/web-stories/title-description.json')
#     data=json.load(file)
   
#     context={}

  
#     for i in data:
#         if i['url']==webno:
#             context['titles']=i
#             return render(request,'web_stories/webstory.html',context)



#web stories
def webstories(request,story):
    context={}
    webno=story
    file=open('media/web-stories/webstory-'+str(webno)+"/webstory-"+str(webno)+".json")
    data=json.load(file)
    context['data']=data
    context['webno']=webno

    file=open('media/web-stories/title-description.json')
    data=json.load(file)
    for i in data:
        if i['url']==webno:
            context['titles']=i
            return render(request,'web_stories/webstory.html',context)


