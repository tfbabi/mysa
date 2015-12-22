#coding=utf8

from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
import json

@login_required
def index(request):
    return render(request,'cache/index.html')

@login_required
def purge(request):
    from purges import purge
    a = purge(request)
    json_result = {'a':a,

            }
    return HttpResponse(json.dumps(json_result,ensure_ascii=False))
