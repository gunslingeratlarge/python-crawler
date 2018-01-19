#!/usr/bin/env python
#-*- coding:utf-8 -*-
import urllib2
import urllib

url = "http://fy.iciba.com/ajax.php?a=fy"
headers = {
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
  "Accept":"application/json, text/javascript, */*; q=0.01",
  "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
  "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
  "X-Requested-With":"XMLHttpRequest",
  "Connection":"keep-alive"
}

key = raw_input("input words: ")
dataform = {
  "f":"auto",
  "t":"auto",
  "w":key
}

data = urllib.urlencode(dataform)
request = urllib2.Request(url, data = data, headers = headers)
response = urllib2.urlopen(request)
print response.read()
