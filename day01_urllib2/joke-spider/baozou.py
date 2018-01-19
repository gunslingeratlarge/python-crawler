#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2
import re 
headers = {
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0"
}

url = "http://baozoumanhua.com/text?page=1"
request = urllib2.Request(url, headers = headers)
response = urllib2.urlopen(request)
html = response.read()
pattern = re.compile('<a href="/articles/\d*" target="_blank">.*?</a>')
jokes = pattern.findall(html)
print jokes
for joke in jokes:
  print joke
