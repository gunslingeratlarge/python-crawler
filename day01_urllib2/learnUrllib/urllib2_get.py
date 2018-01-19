#!/usr/bin/env python
#-*- coding:utf-8 -*-
import urllib2
import urllib
url = "http://www.baidu.com/s"
user_agent = 'Mozilla'

keyword = raw_input('please input your search keyword')
wd = { 'wd':keyword }
wd = urllib.urlencode(wd)
fullurl = url + '?' + wd
print fullurl
request = urllib2.Request(fullurl)
response = urllib2.urlopen(request)
print response.read()
