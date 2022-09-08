from django.contrib.sitemaps import Sitemap
import os,json
from .models import *;

class FullFormView(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=2000
    def items(self):
        return full_form_data.objects.all()
    
    def location(self, item) -> str:
        url="/full-form/"+item.full_form_abbr+"-full-form/"
        return url
