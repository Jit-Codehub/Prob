from django.contrib.sitemaps import Sitemap
from datetime import datetime
from .models import *;
class Guide_Sitemap(Sitemap):
    priority = 0.9
    changefreq = 'monthly'
    limit=2000
    lastmod =datetime(2020, 9, 9)
    def items(self):
        
        return Blog.objects.all()
    def location(self, item):
        return "/guide/"+item.url_slug+"/"