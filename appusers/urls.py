from django.urls import path, include
from .views import *
app_name="appusers"



urlpatterns = [ 
    path('',index,name='index' ),
]