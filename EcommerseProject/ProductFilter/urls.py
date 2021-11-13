from django.urls import path

from .views import *


urlpatterns=[
    path('laptopfiltershow',Laptopfiltershowview,name='Laptopfiltershow'),
    path('mobilefiltershow',Mobilefiltershowview,name='Mobilefiltershow'),
    path('groceryfiltershow',Groceryfiltershowview,name='Groceryfiltershow'),
]
