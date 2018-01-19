#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2

def loadPage(url, filename):
  """
     获得指定url的html文件并返回
  """
  print "获得文件..." + filename
  user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
  request = urllib2.Request(url,headers = {"User-Agent":user_agent})
  response = urllib2.urlopen(request)
  return response.read()

def writePage(html, filename):
  """
     将html文件写到本地
  """   
  print "写入文件..." + filename
  with open(filename,'w') as f:
    f.write(html)  
  print "-" * 30

def tiebaSpider(url, beginPage, endPage):
  """
     贴吧爬虫任务调度器：可以设置爬取哪个贴吧以及页数范围
  """
  for page in range(beginPage, endPage + 1):
    pn = (page - 1) * 50
    fullurl = url + "&pn=" + str(pn)
    filename = "page" + str(page) + ".html"
    html = loadPage(fullurl, filename)
    writePage(html, filename)
  print "爬取结束！"


if __name__ == "__main__":
  keyword = raw_input("please input tieba name :")
  print keyword
  beginPage = int(raw_input("begin page: "))
  endPage = int (raw_input("end page: "))
  url = "http://tieba.baidu.com/f" + "?" + urllib.urlencode({"kw":keyword})
  tiebaSpider(url,beginPage,endPage)    
   


