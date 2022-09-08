from django.shortcuts import render,redirect
# Create your views here.

def aboutus(request):
         return render(request,'base/about_us.html')
def contactus(request):
         return render(request,'base/contact_us.html')

