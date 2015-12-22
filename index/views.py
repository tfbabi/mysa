#coding=utf8
from django.shortcuts import render,get_object_or_404

from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    f = u'真的狠好'
    return render(request,'index/index.html',{'f':f})



    
