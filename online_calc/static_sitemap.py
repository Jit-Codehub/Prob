from django.contrib.sitemaps import Sitemap
from datetime import datetime

class Static_Sitemap(Sitemap):
    priority = 0.9
    changefreq = 'monthly'
    lastmod =datetime(2020, 9, 9)
    def items(self):
        l=[]

        return l
    def location(self, item):
        return (item)

