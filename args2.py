#!/usr/bin/python

from sys import argv

script, first, second = argv

x = raw_input(first + " ")
print '%s is %s' % (first, x)
y = int(raw_input(second + " "))
print '%s is %d' % (second, y)
