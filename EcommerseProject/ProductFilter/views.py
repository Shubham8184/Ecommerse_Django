from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from Seller.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger   
from .filters import LaptopFilter,MobileFilter,GroceryFilter
from django.apps import apps
from django.contrib.postgres import search
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


def Laptopfiltershowview(request):
    records = Laptop.objects.all()
    laptopfilter = LaptopFilter(request.GET, queryset=records)
    rec_per_page = Paginator(laptopfilter.qs, 5)
    page = request.GET.get('page',1)
    # print('PAGE=',page)
    # print(rec_per_page.count)
    # print(rec_per_page.num_pages)
    # print(rec_per_page.page_range)
    try:
        rec = rec_per_page.page(page)
    except PageNotAnInteger:
        rec = rec_per_page.page(1)
    except EmptyPage:
        rec = rec_per_page.page(rec_per_page.num_pages)
    print('filter record', records)
    return render(request, 'ProductFilter/Laptopfiltershow.html', {'records': rec, 'laptopfilter': laptopfilter})

def Mobilefiltershowview(request):
    records = Mobile.objects.all()
    mobilefilter = MobileFilter(request.GET, queryset=records)
    rec_per_page = Paginator(mobilefilter.qs, 5)
    print('PAGINATOR=', rec_per_page)

    page=request.GET.get('page',1)
    print('PAGE=',page)
    print(rec_per_page.count)
    print(rec_per_page.num_pages)
    print(rec_per_page.page_range)

    try:
        rec = rec_per_page.page(page)
    except PageNotAnInteger:
        rec = rec_per_page.page(1)
    except EmptyPage:
        rec = rec_per_page.page(rec_per_page.num_pages)

    return render(request,'ProductFilter/Mobilefiltershow.html',{'records':rec, 'mobilefilter':mobilefilter})

def Groceryfiltershowview(request):
    records = Grocery.objects.all()
    groceryfilter = GroceryFilter(request.GET, queryset=records)
    rec_per_page = Paginator(groceryfilter.qs, 5)
    print('PAGINATOR=', rec_per_page)

    page=request.GET.get('page',1)
    print('PAGE=',page)
    print(rec_per_page.count)
    print(rec_per_page.num_pages)
    print(rec_per_page.page_range)

    try:
        rec = rec_per_page.page(page)
    except PageNotAnInteger:
        rec = rec_per_page.page(1)
    except EmptyPage:
        rec = rec_per_page.page(rec_per_page.num_pages)

    return render(request,'ProductFilter/Groceryfiltershow.html',{'records':rec, 'groceryfilter':groceryfilter})
