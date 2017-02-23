#!/usr/bin/python

import re

l = ["555-8396 Neu, Allison",
     "Burns, C. Montgomery",
     "555-5299 Putz, Lionel",
     "555-7334 Simpson, Homer Jay"]

reg_ex = r"([0-9-]*)\s*([a-zA-Z]+),\s*(.*)"

for i in l:
    res = re.search(reg_ex, i)
    print res.group(3) + ' ' + res.group(2) + ' ' + res.group(1)
