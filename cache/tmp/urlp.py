#!coding=utf8
from urlparse import urlparse

def urlp(urlstr):
    url = urlparse(urlstr)
    hostname = url.hostname
    path = url.path
    return hostname,path
