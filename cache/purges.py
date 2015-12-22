#coding=utf8

from urlparse import urlparse
import requests

def purge(request):
    #获取前端提交的字符串
    #获取并去掉首位空格和换行符
    urlstrs = str(request.POST.get('url','')).strip().split('\r\n') 
    #循环列表并将每个元素的首位空格去掉
    for x in range(len(urlstrs)):
        urlstrs[x] = urlstrs[x].strip()
    #循环去掉列表中空行元素
    while '' in urlstrs:
        urlstrs.remove('')        

    #如果列表为空则返回并提示用户输入
    if len(urlstrs) == 0:
        return "请输入url，谢谢!"
    #print urlstrs

    
    #定义清理url接口调用函数
    def cleanurl(url):
        from .models import apiinfo
        #apiurl = "http://purge.faout.com:8080/clear?url="
        r = apiinfo.objects.get(name="myapi") 
        apiurl = r.url
        requesturl = apiurl+url
        #print requesturl
        r = requests.get(requesturl)
        #print r.text


    #并发向接口发出清理缓存请求
    from multiprocessing.dummy import Pool as ThreadPool 
    pool = ThreadPool()
    results = pool.map(cleanurl,urlstrs)
    pool.close()
    pool.join()


    message = "CDN缓存生效大概10分钟以内生效"
    return message
