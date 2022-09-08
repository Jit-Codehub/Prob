from django.contrib.sitemaps import Sitemap
import os,json

class WebStoryView(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=2000
    def items(self):
        file=open('media/web-stories/title-description.json')
        data=json.load(file)
        return data
    
    def location(self, item) -> str:
        urls="/web-stories/"+item['url']+"/"
        return urls

