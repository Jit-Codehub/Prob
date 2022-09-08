from django.shortcuts import render
import pandas as pd
import requests
from bs4 import BeautifulSoup
from portal.models import *;
from .models import *; 
# Create your views here.
def get_related_data(category,first_letter):
    full_forms=full_form_categories.objects.get(category=category)
    full_forms_data_li=full_form_data.objects.filter(category=full_forms).filter(full_form_abbr__startswith=first_letter)
    return full_forms_data_li
def get_data(category):
    di={}
    full_forms=full_form_categories.objects.get(category=category)
    for i in full_form_data.objects.filter(category=full_forms).values('full_form_abbr','full_form'):
        if i['full_form_abbr'][0] in di:
            di[i['full_form_abbr'][0]].append(i)
        else:
            di[i['full_form_abbr'][0]]=[i]
    return di
def home(request): 
    # di=get_data('Full Forms')
    portal_obj = HomepageBlog.objects.filter(app="full-form",status="Published")
    context = {"portal_obj":portal_obj.first() if portal_obj else None}
    return render(request,'Full_Forms/home.html',context)

def banking(request): 
    di=get_data('Banking')
    return render(request,'Full_Forms/home.html',context={"li":di,"category":'Banking Full Forms'})
def educational(request): 
    di=get_data('Educational')
    return render(request,'Full_Forms/home.html',context={"li":di,"category":'Educational Full Forms'})
def exam(request): 
    di=get_data('Exam')
    return render(request,'Full_Forms/home.html',context={"li":di,"category":'Exam Full Forms'})
def gadget(request): 
    di=get_data('Gadgets')
    return render(request,'Full_Forms/home.html',context={"li":di,"category":'Gadgets Full Forms'})
def internet_slag(request): 
    di=get_data('Internet Slag')
    return render(request,'Full_Forms/home.html',context={"li":di,"category":'Internet Slag Full Forms'})
def medical(request): 
    di=get_data('Medical')
    return render(request,'Full_Forms/home.html',context={"li":di,"category":'Medical Full Forms'})
def it(request): 
    di=get_data('IT')
    return render(request,'Full_Forms/home.html',context={"li":di,"category":'IT Full Forms'})
def telecom(request): 
    di=get_data('Telecom')
    return render(request,'Full_Forms/home.html',context={"li":di,"category":'Telecom Full Forms'})
def organizational(request): 
    di=get_data('Organizational ')
    return render(request,'Full_Forms/home.html',context={"li":di,"category":'Organizational Full Forms'})

def specific_full_form(request,name):
    name=name.split("-")[0]
    li=full_form_data.objects.filter(full_form_abbr=name)[0]
    print(li.category.category)
    related_li=get_related_data(li.category.category,name[0])
    return render(request,'Full_Forms/full-form.html',context={"li":li,'reli':related_li})

def handler404(request,exception):
    return render(request,'Full_Forms/404.html')