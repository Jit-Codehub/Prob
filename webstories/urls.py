from django.urls import path,include
from .views import *

urlpatterns = [
    path('',homepage, name='home'),
    path('<str:story>/',webstories,name='webstories')
]
import webstories.jobs  # NOQA @isort:skip
import logging
logging.basicConfig(level="DEBUG")