#!/usr/bin/python

def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_args(*args):
    print "args[0]: %r, args[1] %r" % (args[0], args[1])

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(*args):
    print 'args[0]: %r' % args[0]

def print_none():
    print "I got nothin'."

print_two('Tomas', 'Kosegi')
print_args('Tomas', 'Kosegi')
print_two_again('Tomas', 'Kosegi')
print_one(100)
print_none()
