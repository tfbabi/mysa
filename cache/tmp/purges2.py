#!coding=utf8

import requests

def purge(hostname,ip,path):
    headers = {'host': hostname}
    url = "http://"+ip+"/purge"+path
    print(hostname)
    print(ip)
    print(url)
    print(headers)

    a = requests.get(url,headers=headers)
    h = a.text
    return h
