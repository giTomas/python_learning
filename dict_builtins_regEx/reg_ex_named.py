#!/usr/bin/python

import re

s = "Sun Oct 14 13:47:03 CEST 2012"
reg_ex = r'\b(?P<hours>\d\d):(?P<minutes>\d\d):(?P<seconds>\d\d)'
match = re.search(reg_ex, s)
print match.group('hours')
print match.group('minutes')
print match.group('seconds')
