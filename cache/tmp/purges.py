#!coding=utf8

import requests
import sys

def purge(request):
    urlstr = str(request.POST.get('url','')).strip()
    #这里进行判断url是否符合要求,假设requests访问没有异常的则执行下面的流程
    try:
        checkcode = int(requests.get(urlstr).status_code)
    except requests.RequestException as e:
        er = "你确定输入的是url地址吗？"
        return er
        sys.exit()

    if checkcode == 200:
        from .models import Domianipinfo
        from django.core.exceptions import ObjectDoesNotExist 
        from .urlp import urlp
        hostname,path = urlp(urlstr)
        print("start")
        try:
            ob = Domianipinfo.objects.get(name=hostname)
        except ObjectDoesNotExist:
            e = hostname+"没有添加ningx缓存功能"
            return e
            sys.exit()

        ips = ob.ip
        iplists = ips.split(',')
        #print("ips: %s" ) % ips
        #print(ips.split(',')[0])
        #print("----------")
        re = ""
        for ip in iplists:
            #print("ip is : %s") % ip
            headers = {'host': hostname}
            url = "http://"+ip+"/purge"+path
            a = requests.get(url,headers=headers)
            re += a.text
        return re
        #print("----------")
    else:
        cc = "输入的url确认能访问吗？"
        return cc
