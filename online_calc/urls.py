from django.contrib import admin
from django.urls import include, path, re_path
from base_files.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from full_forms.views import *
# from Statistics.Sitemap import *

from django.contrib.sitemaps.views import sitemap,index

from PROBABILITY.static_sitemap import *;
from full_forms.full_form_sitemap import *;
from webstories.webstory_sitemap import *;
from django.views.generic import TemplateView
import debug_toolbar
from guide.sitemap import *;
sitemaps = {
    'guide-sitemap':Guide_Sitemap,
    'static':Static_Sitemap,
'web-story-sitemap':WebStoryView,
'full-form-sitemap':FullFormView}

urlpatterns = [
        
    path('about-us/',aboutus, name='about-us'),
    path('contact-us/',contactus, name='contact-us'),
    path('ckeditor/', include(
        'ckeditor_uploader.urls')),
    path('guide/', include('guide.urls')),
    
  
    # path('algebra/',alge, name='alge'),
    
    path('', include('PROBABILITY.urls')),
    path('full-form/', include('full_forms.urls')),
    path('web-stories/', include('webstories.urls')),
    
    
    path('admin/', admin.site.urls),
    path('banking-full-form/',banking, name='banking'),
    path('educational-full-form/',educational, name='educational'),
    path('exam-full-form/',exam, name='exam'),
    path('gadget-full-form/',gadget, name='gadget'),
    path('internet-slag-full-form/',internet_slag, name='internet_slag'),
    path('medical-full-form/',medical, name='medical'),
    path('organizational-full-form/',organizational, name='organizational'),
    path('it-full-form/',it, name='it'),
    path('telecom-full-form/',telecom, name='telecom'),

    ############################# SITEMAP URLS STARTS ######################
    path('sitemap.xml', index, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.index'),
    
    # path('algebra-sitemap.xml', index, {'sitemaps': statistics}, name='django.contrib.sitemaps.views.index'),
    
    path('<section>.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    ############################# SITEMAP URLS STARTS 
    #######################
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'full_forms.views.handler404'



from django.conf import settings

if settings.DEBUG:
    

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls)),]
