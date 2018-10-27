from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

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

def shuzhi(request,p1,p2,p3):
    return HttpResponse('%s,%s,%s'%(p1,p2,p3))

def getTest1(request):
    return render(request,'booktest/test1.html')

def getTest2(request):
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    context = {'a':a1,'b':b1,'c':c1}
    return render(request,'booktest/test2.html',context)

def getTest3(request):
    a1 = request.GET.getlist('a')
    context = {'a': a1}
    return render(request,'booktest/test3.html',context)

def postTest1(request):
    return render(request,'booktest/post1.html')

def postTest2(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST['ugender']
    uhobby = request.POST.getlist('uhobby')
    context = {'uname':uname,'upwd':upwd,'ugender':ugender,'uhobby':uhobby}
    return render(request,'booktest/post2.html',context)

def redTest1(request):
    return redirect('/redTest2')

def redTest2(request):
    return HttpResponse('这是跳转之后的页面')

def session1(request):
    uname = request.session.get('myname','未登录')
    # uname = None
    context = {'name':uname}
    return render(request,'booktest/session1.html',context)
def session2(request):
    return render(request,'booktest/session2.html')
def session2_handle(request):
    uname = request.POST['uname']
    request.session['myname'] = uname
    return redirect('/session1')
def session3(request):
    del request.session['myname']
    return redirect('/session1')









