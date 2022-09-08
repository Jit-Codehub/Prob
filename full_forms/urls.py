from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('<str:name>/',specific_full_form, name='specific_full_form'),
]

# import full_forms.jobs  # NOQA @isort:skip
# import logging
# logging.basicConfig(level="DEBUG")