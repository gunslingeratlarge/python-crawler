#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
pattern = re.compile(r"([a-z]+)-([a-z]+)",re.I)
m = pattern.search("Hell3o-World hello-python")
print "0" + m.group(0)
print "1" + m.group(1)
print "2" + m.group(2)

