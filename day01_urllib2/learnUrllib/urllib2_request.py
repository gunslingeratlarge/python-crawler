#!/usr/bin/env python
#-*- coding:utf-8 -*-
import urllib2
import random

ua_list = [
  "aaa",
  "bbb",
  "ccc"
]

url = "http://www.baidu.com/"
user_agent = random.choice(ua_list)

request = urllib2.Request(url)
request.add_header("User-Agent",user_agent)
ua = request.get_header("User-agent")
print ua
response = urllib2.urlopen(request)
code = response.getcode()
print code
