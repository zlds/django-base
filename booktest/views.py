from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import *
from datetime import datetime
import os

# Create your views here.

def index(request):
    booklist = BookInfo.objects.all()
    context = {'list':booklist}
    return render(request,'booktest/index.html',context)

def show(request,id):
    book = BookInfo.objects.get(pk=id)
    herolist = book.heroinfo_set.all()
    context = {'list':herolist}
    return render(request,'booktest/show.html',context)


def hello(request):
    today = datetime.now().date()
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    # return render(request, "booktest/hello.html", context={"today": today, "days_of_week": daysOfWeek})
    return redirect('http://www.qq.com',permanent=True)

def viewArticle(request, articleId):
    """ A view that display an article based on his ID"""
    text = "Displaying article Number : %s" % articleId
    # return HttpResponse(text)
    return redirect(reverse('articles',kwargs={'year':'2050','month':'12'}))


def viewArticles(request, year, month):
    text = "Displaying articles of : %s/%s" % (year, month)
    return HttpResponse(text)