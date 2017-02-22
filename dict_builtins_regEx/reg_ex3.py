#!/usr/bin/python

import re

fh = open("simpsons_phone_book.txt")
for line in fh:
    if re.search('J.*Neu', line):
        print line.rstrip()

fh.close()
