#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2
import re

class Spider:
  def __init__(self):
    self.page = 1
    self.url = "http://baozoumanhua.com/text?page="
    self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0"}


  def loadPage(self):
    print "正在加载页面..."
    fullurl = self.url + str(self.page)    
    request = urllib2.Request(fullurl, headers = self.headers)
    response = urllib2.urlopen(request)
    html = response.read()
    return html

  def writeJoke(self):
    html = self.loadPage()
    pattern = re.compile('<a href="/articles/\d*" target="_blank">.*?</a>')
    jokes = pattern.findall(html)
    with open("jokes.txt","a") as f:
      for joke in jokes:
        print "正在写入..."
        f.write(re.sub('<a href="/articles/\d*" target="_blank">',"",joke).replace("</a>",""))
        f.write("\n")
        

  def startWork(self):
    begin = int(raw_input("请输入起始页："))
    end = int(raw_input("请输入结束页："))
    if end - begin > 50:
      print "页数过多"
    for i in range(begin, end + 1):
      self.page = i
      self.writeJoke()    
    print "获取完成！"  

if __name__ == "__main__":
  sp = Spider()
  sp.startWork()
