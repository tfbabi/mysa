#!coding=utf8

import requests
from .urlp import urlp


def purge(request):
    urlstr = str(request.POST.get('url',''))
    hostname,path = urlp(urlstr)
    ip = "50.23.174.170"  
    headers = {'host': hostname}
    url = "http://"+ip+"/purge"+path
    print(hostname)
    print(ip)
    print(url)
    print(headers)

    a = requests.get(url,headers=headers)
    h = a.text
    return h
