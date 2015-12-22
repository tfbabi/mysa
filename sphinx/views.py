#coding=utf8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
import json
from .models import Sphinxinfo
#from myparamiko import myexec



@login_required
def index(request):
    fenyeno = 6
    objects = Sphinxinfo.objects
    
    from .fenye import fenYe
    posts,allPage,curPage = fenYe(request,fenyeno,objects)
    addno = fenyeno * (curPage - 1)
    lists = range(1,allPage+1)
    return render(request,'sphinx/index.html',{'posts':posts,'allPage':allPage,'curPage':curPage,'addno':addno,'lists':lists})


@login_required
def indexer(request,id):
    from myparamiko import myExec
    p = get_object_or_404(Sphinxinfo,pk=id)
    r = myExec(p.ip,p.indexerbin,p.conf)    
    json_result = {'id':str(p.id),
                   'content':str(r),

            }
    return HttpResponse(json.dumps(json_result,ensure_ascii=False))
