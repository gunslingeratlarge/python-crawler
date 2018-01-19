#!/usr/bin/env python
#-*- coding:utf-8 -*-
import urllib2
import urllib
wd_my = {'wd':'传智播客'}
encoded = urllib.urlencode(wd_my)
print encoded
decoded = urllib.unquote(encoded)
print decoded
