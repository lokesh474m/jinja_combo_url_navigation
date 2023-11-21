from specific.views import *
from django.urls import path

app_name='specific'

urlpatterns=[

    path('rajmouli/',rajmouli,name='rajmouli'),
    path('tharak/',tharak,name='tharak'),
]