#!/usr/bin/python

from sys import argv

script, textFile = argv

print "Write to file %s" % script
raw_input("?")
target = open(textFile, "w")
target.truncate()
prompt = "> "
line1 = raw_input("line1: " + prompt)
line2 = raw_input("line2: " + prompt)
line3 = raw_input("line3: " + prompt)
nl = "\n"
target.write(line1 + nl + line2 + nl + line3)
target.close()
# file musi byt otvoreny znovu pre flag 'w'
target = open(textFile)
print "New content: "
# nesmie tu chybat print
print target.read()
target.close()
