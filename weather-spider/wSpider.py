#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import datetime
class WSpider:
  def __init__(self):
    #温度url
    self.turl = "http://tianqi.2345.com/shanghai-zhangjiangzhen/97723.htm"
    #空气质量url
    self.aurl = "http://www.86pm25.com/city/shanghai.html"
    self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"} 
  def loadPage(self, url):
    request = urllib2.Request(url, headers = self.headers)
    response = urllib2.urlopen(request)
    return response.read()
 
  def writeTemperature(self):
    html = self.loadPage(self.turl)
    #<div class="inner"><span class="data only"> 阴 <i>6～11℃ </i></span></div>
    pattern = re.compile('''<span class=['"]data only['"]>(.*?)<i>(.*?)</i></span>''',re.S)
    m = pattern.search(html)
    w1 =  m.group(1).decode("gbk").encode("utf-8")
    w2 =  m.group(2).decode("gbk").encode("utf-8")
    now = datetime.datetime.now()
    today = str(now.day)
    with open("todayWeather.txt","w") as f:
      f.write("今日("+ today +"日)张江天气情况：" + w1 + w2 + '\n')
  
  
  def classifyAQI(self, aqi):
    if aqi < 50:
      return "优"
    elif aqi < 100:
      return "良"
    elif aqi < 150:
      return "轻度污染" 
    elif aqi < 200:
      return "重度污染"
    else: 
      return "严重污染"

  def writeAir(self):
    html = self.loadPage(self.aurl)
    pattern = re.compile("<td>浦东张江</td><td>(.*?)</td>",re.S)   
    m = pattern.findall(html)
    aqi = int(m[0])
    with open("todayWeather.txt","a") as f:
      f.write("今日空气质量指数：" + str(aqi) + " " + self.classifyAQI(aqi) + "\n")
  
  def startWork(self):
    self.writeTemperature()
    self.writeAir()
 
    

if __name__ == "__main__":
  s = WSpider()
  s.startWork()
