from django.urls import path
from .views import *

app_name = "guide"

urlpatterns = [
    path('',guide_home, name="home_url"),
    path('<slug:url>/',guide_blog, name="blog_url"),
]