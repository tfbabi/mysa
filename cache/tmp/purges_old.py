#!coding=utf8

import requests

def purge():
    headers = {'host':'www.sammydress.com'}
    a = requests.get("http://50.23.174.170/purge/temp/skin4/images/domeimg/article/DropShipping/men.jpg",headers=headers)
    h = a.text
    return h
