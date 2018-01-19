#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
pattern = re.compile(r"\d+?",re.I)
m = pattern.findall("hello 123456 0988")
print m
